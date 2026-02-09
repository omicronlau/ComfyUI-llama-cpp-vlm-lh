# -*- coding: utf-8 -*-
"""
ComfyUI-llama-cpp-vlmforQo 公共组件
"""
import os
import io
import gc
import json
import base64
import random
import torch
import inspect
import numpy as np
import psutil
import platform
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter

# -------------------------- 自动导入依赖（缺失会提示） --------------------------
try:
    import llama_cpp
    from llama_cpp import Llama
    from llama_cpp.llama_chat_format import (
        Llava15ChatHandler, Llava16ChatHandler, MoondreamChatHandler,
        NanoLlavaChatHandler, Llama3VisionAlphaChatHandler, MiniCPMv26ChatHandler,
        Qwen25VLChatHandler, Qwen3VLChatHandler
    )
except ImportError as e:
    print(f"【错误】缺少llama-cpp-python依赖，请运行：pip install llama-cpp-python")
    exit(1)

try:
    import folder_paths
    import comfy.model_management as mm
    import comfy.utils
except ImportError as e:
    print(f"【错误】未检测到ComfyUI环境，请将该文件放入ComfyUI/custom_nodes/ComfyUI-llama-cpp-vlmforQo/目录下")
    exit(1)

# -------------------------- 硬件检测（保留提速优化） --------------------------
def get_hardware_info():
    hardware_info = {
        "has_cuda": torch.cuda.is_available(),
        "has_rocm": False,
        "gpu_name": "未知显卡",
        "gpu_vram_total": 0.0,
        "gpu_vendor": "unknown",
        "cpu_cores": os.cpu_count() or 4,
        "is_high_perf": False,
        "is_low_perf": True
    }
    
    if hardware_info["has_cuda"]:
        try:
            device_prop = torch.cuda.get_device_properties(0)
            hardware_info["gpu_name"] = device_prop.name
            hardware_info["gpu_vram_total"] = round(device_prop.total_memory / (1024 ** 3), 2)
            hardware_info["gpu_vendor"] = "nvidia"
            
            # 按显存大小和显卡型号分级
            gpu_vram = hardware_info["gpu_vram_total"]
            gpu_name_lower = hardware_info["gpu_name"].lower()
            
            # 高性能显卡标志（24GB+显存）
            high_perf_flags = ["5090", "4090", "3090", "a100", "a10", "rtx 6000", "titan"]
            # 中高性能显卡标志（16GB显存）
            mid_high_perf_flags = ["4080", "3080 ti"]
            # 中性能显卡标志（12GB显存）
            mid_perf_flags = ["4070 ti", "3080", "3070 ti"]
            # 中低性能显卡标志（8GB显存）
            mid_low_perf_flags = ["4070", "3070", "2080 ti", "2080", "1660 ti", "1660 super"]
            
            if gpu_vram >= 24 or any(flag.lower() in gpu_name_lower for flag in high_perf_flags):
                hardware_info["is_high_perf"] = True
                hardware_info["is_low_perf"] = False
                hardware_info["perf_level"] = "high"  # 24GB+
            elif gpu_vram >= 16 or any(flag.lower() in gpu_name_lower for flag in mid_high_perf_flags):
                hardware_info["is_high_perf"] = False
                hardware_info["is_low_perf"] = False
                hardware_info["perf_level"] = "mid_high"  # 16GB
            elif gpu_vram >= 12 or any(flag.lower() in gpu_name_lower for flag in mid_perf_flags):
                hardware_info["is_high_perf"] = False
                hardware_info["is_low_perf"] = False
                hardware_info["perf_level"] = "mid"  # 12GB
            elif gpu_vram >= 8 or any(flag.lower() in gpu_name_lower for flag in mid_low_perf_flags):
                hardware_info["is_high_perf"] = False
                hardware_info["is_low_perf"] = False
                hardware_info["perf_level"] = "mid_low"  # 8GB
            else:
                hardware_info["is_high_perf"] = False
                hardware_info["is_low_perf"] = True
                hardware_info["perf_level"] = "low"  # <8GB
            print(f"【硬件检测】显卡：{hardware_info['gpu_name']}，显存：{hardware_info['gpu_vram_total']}GB")
        except Exception as e:
            print(f"【提示】显卡信息检测失败，自动使用兼容模式：{e}")
    else:
        # 尝试检测AMD显卡（ROCm）
        try:
            if hasattr(torch, 'hip') or hasattr(torch, 'rocm'):
                hardware_info["has_rocm"] = True
                hardware_info["gpu_vendor"] = "amd"
                
                # 尝试获取AMD显卡信息
                try:
                    if hasattr(torch, 'hip'):
                        device_prop = torch.hip.get_device_properties(0)
                    elif hasattr(torch, 'rocm'):
                        device_prop = torch.rocm.get_device_properties(0)
                    else:
                        raise AttributeError("No ROCm device properties available")
                    
                    hardware_info["gpu_name"] = device_prop.name
                    hardware_info["gpu_vram_total"] = round(device_prop.total_memory / (1024 ** 3), 2)
                    
                    # AMD显卡性能分级
                    gpu_vram = hardware_info["gpu_vram_total"]
                    gpu_name_lower = hardware_info["gpu_name"].lower()
                    
                    # 高性能AMD显卡（24GB+显存）
                    amd_high_perf_flags = ["mi300", "mi250", "instinct", "7900 xtx", "7900 xt"]
                    # 中高性能AMD显卡（16GB显存）
                    amd_mid_high_perf_flags = ["7900", "7800 xt", "6950 xt", "6900 xt", "6800 xt"]
                    # 中性能AMD显卡（12GB显存）
                    amd_mid_perf_flags = ["7800", "7700 xt", "6750 xt", "6700 xt", "6600 xt"]
                    # 中低性能AMD显卡（8GB显存）
                    amd_mid_low_perf_flags = ["7700", "7600", "6750", "6700", "6650 xt", "6600", "rx 7600", "rx 6600"]
                    
                    if gpu_vram >= 24 or any(flag.lower() in gpu_name_lower for flag in amd_high_perf_flags):
                        hardware_info["is_high_perf"] = True
                        hardware_info["is_low_perf"] = False
                        hardware_info["perf_level"] = "high"  # 24GB+
                    elif gpu_vram >= 16 or any(flag.lower() in gpu_name_lower for flag in amd_mid_high_perf_flags):
                        hardware_info["is_high_perf"] = False
                        hardware_info["is_low_perf"] = False
                        hardware_info["perf_level"] = "mid_high"  # 16GB
                    elif gpu_vram >= 12 or any(flag.lower() in gpu_name_lower for flag in amd_mid_perf_flags):
                        hardware_info["is_high_perf"] = False
                        hardware_info["is_low_perf"] = False
                        hardware_info["perf_level"] = "mid"  # 12GB
                    elif gpu_vram >= 8 or any(flag.lower() in gpu_name_lower for flag in amd_mid_low_perf_flags):
                        hardware_info["is_high_perf"] = False
                        hardware_info["is_low_perf"] = False
                        hardware_info["perf_level"] = "mid_low"  # 8GB
                    else:
                        hardware_info["is_high_perf"] = False
                        hardware_info["is_low_perf"] = True
                        hardware_info["perf_level"] = "low"  # <8GB
                    
                    print(f"【硬件检测】AMD显卡：{hardware_info['gpu_name']}，显存：{hardware_info['gpu_vram_total']}GB")
                except AttributeError:
                    # 如果无法获取设备属性，尝试使用默认设置
                    hardware_info["gpu_name"] = "AMD GPU (ROCm)"
                    hardware_info["gpu_vram_total"] = 16.0  # 默认值
                    hardware_info["is_high_perf"] = False
                    hardware_info["is_low_perf"] = False
                    hardware_info["perf_level"] = "mid_high"  # 默认中高性能
                    print(f"【硬件检测】检测到AMD ROCm环境，使用默认设置")
            else:
                # 尝试通过系统信息检测AMD显卡
                try:
                    import subprocess
                    if platform.system() == "Windows":
                        # Windows: 使用wmic命令
                        result = subprocess.run(['wmic', 'path', 'win32_VideoController', 'get', 'name'], 
                                           capture_output=True, text=True, timeout=5)
                        gpu_names = result.stdout
                        if 'amd' in gpu_names.lower() or 'radeon' in gpu_names.lower():
                            hardware_info["gpu_vendor"] = "amd"
                            hardware_info["gpu_name"] = "AMD GPU"
                            hardware_info["is_high_perf"] = False
                            hardware_info["is_low_perf"] = False
                            hardware_info["perf_level"] = "mid"  # 默认中性能
                            print(f"【硬件检测】检测到AMD显卡（Windows）")
                    elif platform.system() == "Linux":
                        # Linux: 使用lspci命令
                        result = subprocess.run(['lspci', '-nn'], capture_output=True, text=True, timeout=5)
                        gpu_info = result.stdout
                        if 'amd' in gpu_info.lower() or 'radeon' in gpu_info.lower():
                            hardware_info["gpu_vendor"] = "amd"
                            hardware_info["gpu_name"] = "AMD GPU"
                            hardware_info["is_high_perf"] = False
                            hardware_info["is_low_perf"] = False
                            hardware_info["perf_level"] = "mid"  # 默认中性能
                            print(f"【硬件检测】检测到AMD显卡（Linux）")
                except Exception:
                    pass
                
                if hardware_info["gpu_vendor"] == "unknown":
                    print(f"【硬件检测】未检测到NVIDIA CUDA或AMD ROCm显卡，自动使用CPU/通用显卡兼容模式")
        except Exception as e:
            print(f"【提示】AMD显卡检测失败，自动使用兼容模式：{e}")
    
    print(f"【硬件检测】CPU核心数：{hardware_info['cpu_cores']}")
    return hardware_info

HARDWARE_INFO = get_hardware_info()

# -------------------------- 设置进程高优先级 --------------------------
def set_high_priority():
    try:
        p = psutil.Process()
        if platform.system() == "Windows":
            p.nice(psutil.HIGH_PRIORITY_CLASS)
        else:
            p.nice(max(-10, p.nice() - 5))
        print(f"【优化】已设置进程高优先级，提速更明显")
    except Exception as e:
        print(f"【提示】进程优先级设置失败（不影响核心功能）：{e}")

set_high_priority()

# -------------------------- 初始化ChatHandler（支持所有模型） --------------------------

# 基础模型列表（无需ChatHandler的模型）
base_models = ["LLaVA-1.6", "nanoLLaVA", "llama-joycaption", "moondream3-preview", "Moondream2", 
               "MiniCPM-V-4.5", "GLM-4.6V", "InternLM-XComposer2-VL", "DreamOmni2", 
               "MiniCPM-Llama3-V 2.5", "Llama-3.2-11B-Vision-Instruct", "CogVLM2", 
               "CogVLM-MOE", "Phi-3.5-vision-instruct", "Phi-3-vision-128k-instruct", 
               "Qwen2.5-VL", "Qwen3-VL", "Qwen3-VL-Chat", "Qwen3-VL-Instruct", 
               "LLaMA-3.1-Vision", "Zhipu-Vision", "智谱AI-Vision", "olmOCR-2", 
               "InternVL-1.5", "InternVL-2.0", "Yi-VL-2.0", "Gemma-3", "Granite-DocLing", 
               "Lfm-2-VL", "Llama3-Vision-Alpha", "LLaVA-1.5", "MiniCPM-V-2.6", "Obsidian", 
               "Youtu-VL-4B-Instruct", "EraX-VL-7B-V1.5", "MiMo-VL-7B-RL", "Yi-VL-6B"]

# ChatHandler名称到标准模型名称的映射
CHAT_HANDLER_MODEL_MAP = {
    'qwen25vl': 'Qwen2.5-VL',
    'qwen3vl': 'Qwen3-VL',
    'qwen3vlchat': 'Qwen3-VL-Chat',
    'qwen3vlinstruct': 'Qwen3-VL-Instruct',
    'glm46v': 'GLM-4.6V',
    'minicpmv45': 'MiniCPM-V-4.5',
    'minicpmlama3v25': 'MiniCPM-Llama3-V 2.5',
    'moondream3': 'moondream3-preview',
    'moondream2': 'Moondream2',
    'internlmxcomposer2vl': 'InternLM-XComposer2-VL',
    'dreamomni2': 'DreamOmni2',
    'llama32visioninstruct': 'Llama-3.2-11B-Vision-Instruct',
    'cogvlm2': 'CogVLM2',
    'cogvlmmoe': 'CogVLM-MOE',
    'phi35vision': 'Phi-3.5-vision-instruct',
    'phi3vision128k': 'Phi-3-vision-128k-instruct',
    'llama31vision': 'LLaMA-3.1-Vision',
    'zhipuvision': 'Zhipu-Vision',
    'zhipu-aivision': '智谱AI-Vision',
    'olmocr2': 'olmOCR-2',
    'internvl15': 'InternVL-1.5',
    'internvl20': 'InternVL-2.0',
    'yivl20': 'Yi-VL-2.0',
    'gemma3': 'Gemma-3',
    'granitedocling': 'Granite-DocLing',
    'lfmv2': 'Lfm-2-VL',
    'llama3visionalpha': 'Llama3-Vision-Alpha',
    'llava15': 'LLaVA-1.5',
    'llava16': 'LLaVA-1.6',
    'minicpmv26': 'MiniCPM-V-2.6',
    'minicpmv45': 'MiniCPM-V-4.5',
    'obsidian': 'Obsidian',
    'yutu-vl-4b-instruct': 'Youtu-VL-4B-Instruct',
    'erax-vl-7b-v1.5': 'EraX-VL-7B-V1.5',
    'mimo-vl-7b-rl': 'MiMo-VL-7B-RL',
    'yi-vl-6b': 'Yi-VL-6B',
    'lightonocr-2-1b': 'olmOCR-2'
}

# 动态检测llama_cpp_python中的ChatHandler和模型支持
def detect_available_chat_handlers():
    """自动检测llama_cpp.llama_chat_format中可用的ChatHandler"""
    available_handlers = []
    detected_models = []
    
    try:
        import llama_cpp.llama_chat_format
        
        # 扫描所有以ChatHandler结尾的类
        for attr_name in dir(llama_cpp.llama_chat_format):
            if attr_name.endswith('ChatHandler'):
                available_handlers.append(attr_name)
                
                # 根据命名规则推断模型名称
                # 示例：Qwen3VLChatHandler -> Qwen3-VL
                # 示例：Llama32VisionInstructChatHandler -> Llama-3.2-Vision-Instruct
                model_name = attr_name.replace('ChatHandler', '')
                
                # 处理命名规则
                import re
                # 添加连字符
                model_name = re.sub(r'([a-z])([A-Z])', r'\1-\2', model_name)
                model_name = re.sub(r'([0-9])([A-Z])', r'\1-\2', model_name)
                model_name = re.sub(r'([A-Z])([0-9])', r'\1-\2', model_name)
                
                # 转换为小写，然后处理特殊情况
                model_name = model_name.lower()
                
                # 应用特殊处理
                if model_name in CHAT_HANDLER_MODEL_MAP:
                    detected_model = CHAT_HANDLER_MODEL_MAP[model_name]
                else:
                    # 保持原始转换结果
                    detected_model = model_name.title().replace('-', ' ')
                
                detected_models.append(detected_model)
        
        print(f"【模型检测】发现{len(available_handlers)}个可用的ChatHandler")
        print(f"【模型检测】推断出{len(detected_models)}个模型")
        
    except ImportError as e:
        print(f"【模型检测】无法导入llama_cpp.llama_chat_format：{e}")
    except Exception as e:
        print(f"【模型检测】检测过程出错：{e}")
    
    return available_handlers, detected_models

# 执行模型检测
available_handlers, detected_models = detect_available_chat_handlers()

# 生成chat_handlers列表
chat_handlers = ["None"] + base_models + detected_models

# 去重，保持顺序
seen = set()
chat_handlers = [x for x in chat_handlers if not (x in seen or seen.add(x))]

# 确保所有检测到的模型都在chat_handlers列表中
for model in detected_models:
    if model not in chat_handlers:
        chat_handlers.append(model)

# 再次去重，确保没有重复
seen = set()
chat_handlers = [x for x in chat_handlers if not (x in seen or seen.add(x))]

print(f"【模型列表】最终生成了{len(chat_handlers)}个模型选项")
print(f"【模型列表】前10个模型：{chat_handlers[:10]}")

# 动态构建模型信息
all_models = []
for handler_name in available_handlers:
    # 推断模型名称
    model_name = handler_name.replace('ChatHandler', '')
    import re
    model_name = re.sub(r'([a-z])([A-Z])', r'\1-\2', model_name)
    model_name = re.sub(r'([0-9])([A-Z])', r'\1-\2', model_name)
    model_name = re.sub(r'([A-Z])([0-9])', r'\1-\2', model_name)
    model_name = model_name.lower()
    
    if model_name in CHAT_HANDLER_MODEL_MAP:
        detected_model = CHAT_HANDLER_MODEL_MAP[model_name]
    else:
        detected_model = model_name.title().replace('-', ' ')
    
    # 检查是否是Qwen模型
    is_qwen = 'qwen' in model_name.lower()
    
    all_models.append({
        "handler": handler_name,
        "models": [detected_model],
        "is_qwen": is_qwen
    })

# 初始化所有ChatHandler为None
for model_info in all_models:
    globals()[model_info["handler"]] = None

# 动态导入所有ChatHandler
for model_info in all_models:
    handler_name = model_info["handler"]
    models = model_info["models"]
    is_qwen = model_info["is_qwen"]
    
    try:
        # 动态导入ChatHandler
        exec(f"from llama_cpp.llama_chat_format import {handler_name}")
        print(f"【模型支持】成功兼容{models[0]}模型")
    except ImportError as e:
        # 统一的错误处理方式
        print(f"【模型支持】{models[0]}模型暂不兼容（忽略，不影响其他功能）")
        print(f"【详细信息】{type(e).__name__}: {e}")


# -------------------------- 通用工具类 --------------------------
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

def image2base64(image):
    img = Image.fromarray(image)
    buffered = io.BytesIO()
    jpeg_quality = 70 if HARDWARE_INFO["is_low_perf"] else 75
    optimize = True if HARDWARE_INFO["is_high_perf"] else False
    img.save(buffered, format="JPEG", quality=jpeg_quality, optimize=optimize)
    img_base64 = base64.b64encode(buffered.getbuffer()).decode('utf-8')
    return img_base64

def scale_image(image: torch.Tensor, max_size: int = 128):
    try:
        img_np = np.clip(255.0 * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
        img_pil = Image.fromarray(img_np)
        w, h = img_pil.size
        scale = min(max_size / max(w, h), 1.0)
        if scale < 1.0:
            new_w = int(w * scale)
            new_h = int(h * scale)
            resample_mode = Image.Resampling.LANCZOS if HARDWARE_INFO["cpu_cores"] >= 8 else Image.Resampling.BILINEAR
            img_pil = img_pil.resize((new_w, new_h), resample=resample_mode)
        img_np = np.array(img_pil)
        return img_np
    except Exception as e:
        print(f"【错误】图片缩放失败：{e}")
        return np.array(Image.fromarray(np.clip(255.0 * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)))

def parse_json(json_str):
    try:
        if isinstance(json_str, str):
            return json.loads(json_str)
        return json_str
    except Exception as e:
        print(f"【错误】解析JSON失败：{e}")
        return {}

def qwen3bbox(image, json_data):
    bbox_list = []
    img_np = np.array(image)
    h, w, _ = img_np.shape
    
    try:
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        if isinstance(json_data, list):
            for item in json_data:
                if isinstance(item, dict) and "bbox" in item:
                    bbox = item["bbox"]
                    label = item.get("label", "object")
                    x1, y1, x2, y2 = map(int, bbox)
                    bbox_list.append({"bbox_2d": [x1, y1, x2, y2], "label": label})
    except Exception as e:
        print(f"【错误】解析Qwen3边界框失败：{e}")
    
    return bbox_list

def draw_bbox(image, json_data, mode):
    try:
        img_np = np.array(image)
        img_pil = Image.fromarray(img_np)
        draw = ImageDraw.Draw(img_pil)
        
        if mode == "Qwen3-VL":
            bbox_list = qwen3bbox(img_pil, json_data)
        elif mode == "simple":
            bbox_list = parse_json(json_data)
            if not isinstance(bbox_list, list):
                return img_np
        else:
            bbox_list = parse_json(json_data)
            if not isinstance(bbox_list, list):
                return img_np
        
        for bbox_item in bbox_list:
            if isinstance(bbox_item, dict) and "bbox_2d" in bbox_item:
                bbox = bbox_item["bbox_2d"]
                label = bbox_item.get("label", "object")
                x1, y1, x2, y2 = bbox
                draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
                draw.text((x1, y1 - 20), label, fill="red", font=None)
    except Exception as e:
        print(f"【错误】绘制边界框失败：{e}")
    
    return np.array(img_pil)

# -------------------------- 模型存储类（单例模式） --------------------------
class LLAMA_CPP_STORAGE:
    llm = None
    chat_handler = None
    current_config = None
    messages = {}
    sys_prompts = {}
    
    @classmethod
    def clean_state(cls, id=-1):
        if id == -1:
            cls.messages.clear()
            cls.sys_prompts.clear()
            print(f"【会话管理】已清理所有会话状态")
        else:
            cls.messages.pop(f"{id}", None)
            cls.sys_prompts.pop(f"{id}", None)
            print(f"【会话管理】已清理会话状态 (id={id})")
    
    @classmethod
    def clean(cls, all=False):
        try:
            if cls.llm is not None:
                cls.llm.close()
                print(f"【资源释放】成功关闭LLM模型")
        except Exception as e:
            print(f"【提示】关闭LLM模型失败（忽略，继续释放资源）：{e}")
        
        if cls.chat_handler is not None:
            release_methods = [("_exit_stack", lambda x: x.close()), ("close", lambda x: x()), ("cleanup", lambda x: x())]
            for attr, func in release_methods:
                if hasattr(cls.chat_handler, attr):
                    try:
                        func(getattr(cls.chat_handler, attr))
                        print(f"【资源释放】成功释放ChatHandler资源")
                    except Exception as e:
                        print(f"【提示】释放ChatHandler资源失败（忽略）：{e}")
                    break
        
        cls.llm = None
        cls.chat_handler = None
        cls.current_config = None
        
        if all:
            cls.clean_state()
    
    @classmethod
    def get_chat_handler_cls(cls, chat_handler_name):
        try:
            if chat_handler_name == "None":
                return None
            elif chat_handler_name == "LLaVA-1.6":
                return Llava16ChatHandler
            elif chat_handler_name == "nanoLLaVA":
                return NanoLlavaChatHandler
            elif chat_handler_name == "MiniCPM-V-4.5" and MiniCPMv45ChatHandler is not None:
                return MiniCPMv45ChatHandler
            elif chat_handler_name == "Qwen2.5-VL" and Qwen25VLChatHandler is not None:
                return Qwen25VLChatHandler
            elif "Qwen3-VL" in chat_handler_name and Qwen3VLChatHandler is not None:
                return Qwen3VLChatHandler
            elif chat_handler_name == "GLM-4.6V" and GLM46VChatHandler is not None:
                return GLM46VChatHandler
            elif chat_handler_name == "GLM-4.1V-Thinking" and GLM41VChatHandler is not None:
                return GLM41VChatHandler
            elif chat_handler_name == "moondream3-preview":
                if Moondream3ChatHandler is not None:
                    return Moondream3ChatHandler
                return MoondreamChatHandler
            elif chat_handler_name == "Moondream2":
                if Moondream2ChatHandler is not None:
                    return Moondream2ChatHandler
                return MoondreamChatHandler
            elif chat_handler_name == "InternLM-XComposer2-VL":
                if InternLMXComposer2VLChatHandler is not None:
                    return InternLMXComposer2VLChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "DreamOmni2":
                if DreamOmni2ChatHandler is not None:
                    return DreamOmni2ChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "MiniCPM-Llama3-V 2.5":
                if MiniCPMLlama3V25ChatHandler is not None:
                    return MiniCPMLlama3V25ChatHandler
                return MiniCPMv26ChatHandler
            elif chat_handler_name == "Llama-3.2-11B-Vision-Instruct":
                if Llama32VisionInstructChatHandler is not None:
                    return Llama32VisionInstructChatHandler
                return Llama3VisionAlphaChatHandler
            elif chat_handler_name == "CogVLM2":
                if CogVLM2ChatHandler is not None:
                    return CogVLM2ChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "CogVLM-MOE":
                if CogVLMMOEChatHandler is not None:
                    return CogVLMMOEChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "Phi-3.5-vision-instruct":
                if Phi35VisionChatHandler is not None:
                    return Phi35VisionChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "Phi-3-vision-128k-instruct":
                if Phi3Vision128kChatHandler is not None:
                    return Phi3Vision128kChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "LLaMA-3.1-Vision":
                if Llama31VisionChatHandler is not None:
                    return Llama31VisionChatHandler
                return Llama3VisionAlphaChatHandler
            elif chat_handler_name == "Zhipu-Vision" or chat_handler_name == "智谱AI-Vision":
                if ZhipuVisionChatHandler is not None:
                    return ZhipuVisionChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "olmOCR-2":
                if OlmOCR2ChatHandler is not None:
                    return OlmOCR2ChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "InternVL-1.5":
                if InternVL15ChatHandler is not None:
                    return InternVL15ChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "InternVL-2.0":
                if InternVL20ChatHandler is not None:
                    return InternVL20ChatHandler
                return Llava16ChatHandler
            elif chat_handler_name == "Yi-VL-2.0":
                if YiVL20ChatHandler is not None:
                    return YiVL20ChatHandler
                return Llava16ChatHandler
            else:
                print(f"【提示】未找到匹配的ChatHandler：{chat_handler_name}，使用默认处理")
                return None
        except Exception as e:
            print(f"【错误】获取ChatHandler失败：{e}")
            return None
    
    @classmethod
    def init_chat_handler(cls, handler_cls, mmproj_path, chat_handler_name, image_max_tokens, image_min_tokens):
        if handler_cls is None:
            return None
        
        try:
            import inspect
            print(f"【调试】初始化ChatHandler：{handler_cls.__name__}")
            
            # 针对Qwen3-VL的特殊处理
            if "Qwen3-VL" in chat_handler_name:
                print(f"【调试】Qwen3-VL特殊处理")
                
                # 尝试多种备选方案
                backup_handlers = [
                    ("Qwen3VLChatHandler", handler_cls),
                    ("Llava15ChatHandler", None),
                    ("Llava16ChatHandler", None),
                    ("Llama3VisionAlphaChatHandler", None),
                    ("MiniCPMv26ChatHandler", None),
                    ("MoondreamChatHandler", None)
                ]
                
                for handler_name, backup_cls in backup_handlers:
                    try:
                        # 如果是第一个处理（Qwen3-VL），直接使用提供的handler_cls
                        # 否则，动态导入备份ChatHandler
                        if backup_cls is None:
                            from llama_cpp.llama_chat_format import Llava15ChatHandler, Llava16ChatHandler, Llama3VisionAlphaChatHandler, MiniCPMv26ChatHandler, MoondreamChatHandler
                            backup_cls = locals()[handler_name]
                        
                        if backup_cls is None:
                            continue
                            
                        print(f"【调试】尝试使用{backup_cls.__name__}初始化")
                        
                        # 构建初始化参数
                        init_params = {"verbose": False}
                        if mmproj_path:
                            # 检查参数名
                            try:
                                sig = inspect.signature(backup_cls.__init__)
                                if "mmproj" in sig.parameters:
                                    init_params["mmproj"] = mmproj_path
                                elif "clip_model_path" in sig.parameters:
                                    init_params["clip_model_path"] = mmproj_path
                                print(f"【调试】添加参数：{list(init_params.keys())}")
                            except Exception:
                                # 如果无法获取签名，尝试两种参数名
                                try:
                                    init_params["mmproj"] = mmproj_path
                                except Exception:
                                    init_params.pop("mmproj", None)
                                    init_params["clip_model_path"] = mmproj_path
                        
                        # 初始化ChatHandler
                        chat_handler = backup_cls(**init_params)
                        print(f"【成功】已使用{backup_cls.__name__}初始化ChatHandler！")
                        return chat_handler
                    except Exception as e:
                        print(f"【错误】{handler_name}初始化失败：{type(e).__name__}: {e}")
                        # 不打印完整堆栈，避免输出过多
                        continue
            
            # 通用ChatHandler初始化
            print(f"【调试】通用ChatHandler初始化")
            
            # 获取ChatHandler构造函数的参数签名
            sig = inspect.signature(handler_cls.__init__)
            init_params = {"verbose": False}
            
            # 检查并添加可用的参数
            if "clip_model_path" in sig.parameters or "mmproj" in sig.parameters:
                if mmproj_path:
                    # 根据不同ChatHandler的参数名选择合适的参数
                    if "clip_model_path" in sig.parameters:
                        init_params["clip_model_path"] = mmproj_path
                        print(f"【调试】添加参数：clip_model_path={mmproj_path}")
                    else:
                        init_params["mmproj"] = mmproj_path
                        print(f"【调试】添加参数：mmproj={mmproj_path}")
            
            if "image_max_tokens" in sig.parameters and "image_min_tokens" in sig.parameters:
                if image_max_tokens > 0:
                    init_params["image_max_tokens"] = image_max_tokens
                    print(f"【调试】添加参数：image_max_tokens={image_max_tokens}")
                if image_min_tokens > 0:
                    init_params["image_min_tokens"] = image_min_tokens
                    print(f"【调试】添加参数：image_min_tokens={image_min_tokens}")
            
            print(f"【调试】最终初始化参数：{init_params}")
            chat_handler = handler_cls(**init_params)
            print(f"【成功】通用ChatHandler初始化成功：{handler_cls.__name__}")
            return chat_handler
        except Exception as e:
            print(f"【错误】初始化ChatHandler失败：{e}")
            # 提供友好的错误信息和解决方案
            raise ValueError(f"【错误】初始化ChatHandler失败：{chat_handler_name}\n" \
                          f"可能的原因：\n" \
                          f"1. llama-cpp-python版本过低，不支持Qwen3-VL\n" \
                          f"2. MMProj文件与ChatHandler不兼容\n" \
                          f"3. 模型可能需要更新的llama-cpp-python版本\n" \
                          f"\n解决建议：\n" \
                          f"- 更新llama-cpp-python到最新版本\n" \
                          f"- 尝试使用其他ChatHandler（如LLaVA-1.5）\n" \
                          f"- 检查MMProj文件是否与模型匹配") from e
    
    @classmethod
    def load_model(cls, config):
        try:
            # 首先释放旧的模型资源，避免资源冲突
            print(f"【模型加载】开始加载新模型，正在释放旧资源...")
            cls.clean()
            
            model = config["model"]
            enable_mmproj = config["enable_mmproj"]
            mmproj = config["mmproj"]
            chat_handler_name = config["chat_handler"]
            device_mode = config.get("device_mode", "GPU")  # 默认使用 GPU 模式
            n_ctx = config["n_ctx"]
            n_gpu_layers = config["n_gpu_layers"]
            vram_limit = config["vram_limit"]
            image_min_tokens = config["image_min_tokens"]
            image_max_tokens = config["image_max_tokens"]
            
            # 根据设备模式调整参数
            if device_mode == "CPU":
                # CPU 模式：忽略 GPU 相关参数，强制使用纯 CPU
                print(f"【设备模式】使用 CPU 模式（忽略 n_gpu_layers 和 vram_limit 参数）")
                n_gpu_layers = 0
                vram_limit = -1
            else:
                # GPU 模式：使用用户设置的参数
                print(f"【设备模式】使用 GPU 模式（n_gpu_layers={n_gpu_layers}, vram_limit={vram_limit}GB）")
            
            # 构建模型路径
            model_path = os.path.join(folder_paths.models_dir, 'LLM', model)
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"模型文件不存在：{model_path}")
            
            # 构建MMProj路径
            mmproj_path = None
            if enable_mmproj and mmproj != "None":
                mmproj_path = os.path.join(folder_paths.models_dir, 'LLM', mmproj)
                if not os.path.exists(mmproj_path):
                    raise FileNotFoundError(f"MMProj文件不存在：{mmproj_path}")
            
            # 获取模型格式
            model_ext = os.path.splitext(model)[1].lower()
            if model_ext not in [".gguf", ".gguf", ".safetensors"]:
                print(f"【提示】模型格式可能不支持：{model_ext}，将尝试加载")
            
            # 获取并初始化ChatHandler
            handler_cls = cls.get_chat_handler_cls(chat_handler_name)
            cls.chat_handler = cls.init_chat_handler(handler_cls, mmproj_path, chat_handler_name, image_max_tokens, image_min_tokens)
            
            if enable_mmproj:
                if chat_handler_name == "None":
                    raise ValueError(f"【错误】启用了MMProj但未选择ChatHandler，请选择对应的ChatHandler（如Qwen3-VL）")
                
                if handler_cls is None:
                    raise ValueError(f"【错误】无法找到ChatHandler：{chat_handler_name}，请确保选择了正确的ChatHandler")
                
                if cls.chat_handler is None:
                    # 尝试使用默认的视觉ChatHandler作为备选
                    print(f"【调试】尝试使用默认视觉ChatHandler作为备选...")
                    try:
                        from llama_cpp.llama_chat_format import Llava15ChatHandler
                        cls.chat_handler = Llava15ChatHandler(mmproj=mmproj_path, verbose=False)
                        print(f"【成功】已使用Llava15ChatHandler作为备选")
                    except Exception as e:
                        print(f"【错误】备选ChatHandler也初始化失败：{e}")
                        raise ValueError(f"【错误】初始化ChatHandler失败：{chat_handler_name}，请检查MMProj文件和ChatHandler是否兼容\n" \
                                        f"可能的原因：\n" \
                                        f"1. llama-cpp-python版本过低，不支持Qwen3-VL\n" \
                                        f"2. MMProj文件与ChatHandler不兼容\n" \
                                        f"3. ChatHandler类需要特定的参数配置") from e
                
                print(f"【成功】已启用MMProj并初始化ChatHandler：{type(cls.chat_handler).__name__}")
            
            # 加载LLM模型前的智能检查
            print(f"【模型加载】开始加载LLM模型：{model}（上下文：{n_ctx}，GPU层数：{n_gpu_layers}）")
            
            # 计算推荐的最大GPU层数（仅在 GPU 模式下）
            recommended_gpu_layers = n_gpu_layers
            if device_mode == "GPU" and (HARDWARE_INFO["has_cuda"] or HARDWARE_INFO["has_rocm"]) and n_gpu_layers > 0:
                # 根据显存大小计算推荐的GPU层数
                gpu_vram = HARDWARE_INFO["gpu_vram_total"]
                gpu_vendor = HARDWARE_INFO["gpu_vendor"]
                
                # 估算模型在GPU中占用的显存（包括上下文）
                estimated_vram_usage = 0
                try:
                    model_file_size = os.path.getsize(model_path) / (1024 ** 3)  # GB
                    # AMD ROCm的显存开销略高于NVIDIA CUDA
                    vram_multiplier = 1.9 if gpu_vendor == "amd" else 1.8
                    estimated_vram_usage = model_file_size * vram_multiplier
                    
                    if enable_mmproj and mmproj != "None":
                        mmproj_file_size = os.path.getsize(os.path.join(folder_paths.models_dir, 'LLM', mmproj)) / (1024 ** 3)
                        estimated_vram_usage += mmproj_file_size * 1.2
                    
                    # 预留显存给系统和其他进程（AMD需要更多预留）
                    reserved_vram = 2.0 if gpu_vendor == "amd" else 1.5
                    available_vram = gpu_vram - reserved_vram
                    
                    if estimated_vram_usage > available_vram and n_gpu_layers == -1:
                        # 如果模型需要的显存超过可用显存，自动降低GPU层数
                        recommended_gpu_layers = int(n_gpu_layers * (available_vram / estimated_vram_usage))
                        recommended_gpu_layers = max(0, recommended_gpu_layers)
                        
                        print(f"【显存警告】模型预计需要{estimated_vram_usage:.2f}GB显存，可用{available_vram:.2f}GB")
                        print(f"【智能建议】建议将GPU层数调整为{recommended_gpu_layers}层")
                        print(f"【提示】您可以通过降低n_ctx、减少max_tokens或使用更小的模型来解决显存问题")
                except Exception as e:
                    print(f"【提示】显存估算失败，使用默认设置：{e}")
            elif device_mode == "CPU":
                # CPU 模式：不需要显存估算
                print(f"【提示】CPU 模式：跳过显存估算")
            
            # 构建模型参数
            gpu_vendor = HARDWARE_INFO["gpu_vendor"]
            
            # 根据GPU厂商和性能级别调整参数
            if gpu_vendor == "amd":
                # AMD ROCm优化参数
                n_batch = 1024  # AMD ROCm的批处理大小较小
                n_threads = os.cpu_count() or 8
                n_threads_batch = os.cpu_count() or 8
                use_mmap = False  # AMD ROCm通常不需要mmap
                use_mlock = True  # AMD ROCm建议使用mlock
                f16_kv = True  # AMD ROCm支持f16 KV缓存
                low_vram = HARDWARE_INFO["is_low_perf"]
            else:
                # NVIDIA CUDA优化参数
                n_batch = 2048
                n_threads = os.cpu_count() or 8
                n_threads_batch = os.cpu_count() or 16
                use_mmap = True
                use_mlock = False
                f16_kv = True
                low_vram = HARDWARE_INFO["is_low_perf"]
            
            llama_kwargs = {
                "model_path": model_path,
                "chat_handler": cls.chat_handler,
                "n_gpu_layers": recommended_gpu_layers,
                "n_ctx": n_ctx,
                "n_batch": n_batch,
                "verbose": False,
                "n_threads": n_threads,
                "n_threads_batch": n_threads_batch,
                "low_vram": low_vram if device_mode == "GPU" else True,  # CPU 模式强制启用低显存模式
                "tensor_split": None,
                "use_mmap": use_mmap,
                "use_mlock": use_mlock,
                "f16_kv": f16_kv,
            }
            
            # AMD ROCm特定优化
            if gpu_vendor == "amd":
                print(f"【AMD优化】应用ROCm特定优化参数")
                print(f"【AMD优化】n_batch={n_batch}, n_threads={n_threads}, n_threads_batch={n_threads_batch}")
                print(f"【AMD优化】use_mmap={use_mmap}, use_mlock={use_mlock}, f16_kv={f16_kv}")
            else:
                print(f"【NVIDIA优化】应用CUDA特定优化参数")
                print(f"【NVIDIA优化】n_batch={n_batch}, n_threads={n_threads}, n_threads_batch={n_threads_batch}")
            
            # 尝试加载模型，失败时提供降级策略
            try:
                # 暂时重定向标准输出，每加载50个参数显示一条摘要
                import sys
                original_stdout = sys.stdout
                original_stderr = sys.stderr
                
                # 创建一个自定义输出流，用于捕获和处理加载信息
                class LoadingOutput:
                    def __init__(self):
                        self.buffer = []
                        self.param_count = 0
                        self.last_percent = -1
                    
                    def write(self, text):
                        # 捕获所有输出
                        self.buffer.append(text)
                        
                        # 尝试提取参数加载信息
                        if "Loading weights:" in text:
                            try:
                                # 提取百分比和参数计数
                                if "|" in text:
                                    parts = text.split("|")
                                    # 查找包含参数计数的部分，如 "1/258"
                                    for part in parts:
                                        if "/" in part:
                                            count_str = part.strip()
                                            if count_str and count_str[0].isdigit():
                                                current = int(count_str.split("/")[0])
                                                total = int(count_str.split("/")[1])
                                                
                                                # 每50个参数或百分比变化时显示一条日志
                                                if current % 50 == 0 or (current > 0 and current % 10 == 0 and current < 100):
                                                    percent = int((current / total) * 100)
                                                    if percent != self.last_percent:
                                                        print(f"【模型加载】进度：{percent}%，参数：{current}/{total}")
                                                        self.last_percent = percent
                                    
                            except Exception:
                                pass
                    
                    def flush(self):
                        pass
                
                loading_output = LoadingOutput()
                sys.stdout = loading_output
                sys.stderr = loading_output
                
                try:
                    cls.llm = Llama(**llama_kwargs)
                finally:
                    # 恢复标准输出
                    sys.stdout = original_stdout
                    sys.stderr = original_stderr
                
                print(f"【模型加载】LLM模型加载成功！（格式：{model_ext}）")
            except Exception as e:
                error_msg = str(e)
                
                # 分析错误类型，提供针对性建议
                if "out of memory" in error_msg.lower() or "oom" in error_msg.lower():
                    # 显存不足错误
                    print(f"【显存错误】加载模型失败：{error_msg}")
                    print(f"【智能建议】")
                    print(f"  1. 降低n_gpu_layers值（当前：{recommended_gpu_layers}）")
                    print(f"  2. 减少n_ctx值（当前：{n_ctx}）")
                    print(f"  3. 使用更小的模型或更高压缩率的量化版本")
                    print(f"  4. 关闭mmproj（如果不需要多模态功能）")
                    
                    # 尝试降级加载（纯CPU）
                    print(f"【尝试降级】尝试使用纯CPU模式加载模型...")
                    llama_kwargs["n_gpu_layers"] = 0
                    llama_kwargs["low_vram"] = True
                    
                    try:
                        # 再次重定向标准输出，使用相同的加载输出处理
                        import sys
                        original_stdout = sys.stdout
                        original_stderr = sys.stderr
                        
                        # 创建一个自定义输出流，用于捕获和处理加载信息
                        class LoadingOutput:
                            def __init__(self):
                                self.buffer = []
                                self.param_count = 0
                                self.last_percent = -1
                            
                            def write(self, text):
                                # 捕获所有输出
                                self.buffer.append(text)
                                
                                # 尝试提取参数加载信息
                                if "Loading weights:" in text:
                                    try:
                                        # 提取百分比和参数计数
                                        if "|" in text:
                                            parts = text.split("|")
                                            # 查找包含参数计数的部分，如 "1/258"
                                            for part in parts:
                                                if "/" in part:
                                                    count_str = part.strip()
                                                    if count_str and count_str[0].isdigit():
                                                        current = int(count_str.split("/")[0])
                                                        total = int(count_str.split("/")[1])
                                                        
                                                        # 每50个参数或百分比变化时显示一条日志
                                                        if current % 50 == 0 or (current > 0 and current % 10 == 0 and current < 100):
                                                            percent = int((current / total) * 100)
                                                            if percent != self.last_percent:
                                                                print(f"【模型加载】(CPU模式) 进度：{percent}%，参数：{current}/{total}")
                                                                self.last_percent = percent
                                    
                                    except Exception:
                                        pass
                            
                            def flush(self):
                                pass
                        
                        loading_output = LoadingOutput()
                        sys.stdout = loading_output
                        sys.stderr = loading_output
                        
                        try:
                            cls.llm = Llama(**llama_kwargs)
                        finally:
                            # 恢复标准输出
                            sys.stdout = original_stdout
                            sys.stderr = original_stderr
                        
                        print(f"【模型加载】LLM模型已使用纯CPU模式加载成功！")
                        print(f"【提示】CPU模式推理速度会较慢，建议使用更小的模型以提高速度")
                    except Exception as fallback_e:
                        raise RuntimeError(f"【错误】加载LLM模型失败（包括降级尝试）：{fallback_e}") from fallback_e
                else:
                    # 其他类型错误
                    raise RuntimeError(f"【错误】加载LLM模型失败：{e}") from e
            
            cls.current_config = config
        except Exception as e:
            print(f"【错误】加载模型失败：{e}")
            raise
