# ComfyUI-llama-cpp-vlmforQo

在ComfyUI中基于llama.cpp原生运行LLM/VLM模型，支持多模态推理、视觉语言理解和各种AI任务。  
**\[**[**📃English**](./README.md)**]**

## 项目简介

ComfyUI-llama-cpp-vlmforQo是一个功能强大的ComfyUI插件，基于ComfyUI-llama-cpp-vlm插件进行的功能新增与性能优化，允许用户在本地运行各种大型语言模型(LLM)和视觉语言模型(VLM)，无需依赖云服务。该插件基于llama.cpp技术，提供高效的模型推理能力，支持从高端到低端显卡的广泛设备。【与ComfyUI-llama-cpp-vlm等分支插件不兼容，如果节点无法正常使用，请重新将节点添加到工作流中】

## 核心功能

- **多模态支持**：处理文本、图片和视频输入
- **广泛的模型兼容性**：支持20+种主流VLM/LLM模型
- **智能硬件适配**：根据显存大小自动调整参数
- **高效推理**：优化的模型加载和推理流程
- **丰富的预设模板**：内置多种提示词模板
- **灵活的参数控制**：详细的推理参数设置
- **会话管理**：支持会话状态保存和清理

## 中文翻译
将zh-CN文件放入翻译插件(ComfyUI-Chinese-Translation/AIGODLIKE-ComfyUI-Translation/ComfyUI-DD-Translation对)应的文件夹内覆盖即可,推荐安装ComfyUI-Chinese-Translation插件，汉化更全面，翻译更新速度更快更全。

## 支持的模型

### 静态支持的模型
- "LLaVA-1.5", "LLaVA-1.6", "Moondream2", "nanoLLaVA"
- "llama3-Vision-Alpha", "MiniCPM-v2.6", "MiniCPM-v4", "MiniCPM-V-4.5"
- "LFM2.5-VL", "GLM-4.6V", "llama-joycaption"

### 动态导入的模型（根据llama-cpp-python版本）
- "Gemma3", "Qwen2.5-VL", "Qwen3-VL", "Qwen3-VL-Chat", "Qwen3-VL-Instruct"
- "GLM-4.1V-Thinking", "LFM2-VL", "MobileVLM", "TinyLLaVA", "MiniGPT-v2"

- 插件已支持 LFM2.5-VL模型加载，llama_cpp_python暂不兼容

## 更新日志
#### 2026-01-29
- 重构了文件目录，安装时需删除旧版文件，请勿覆盖
- 新增专业AI模型的全面预设提示词模板：
  - **ZIMAGE - Turbo**：专为 Z-Image-Turbo 模型优化，支持8步Turbo推理快速生成1080P高清图像
  - **FLUX2 - Klein**：专为 FLUX 系列（Flux.1 和 FLUX.2 Klein）模型设计，创建简洁而富有表现力的提示词
  - **LTX-2**：专为 LTX-2 视频生成模型定制，支持动态视频提示词，可生成高质量、音画同步的4K视频
  - **Qwen - Image Layered**：为 Qwen-Image-Layered 模型创建，支持详细分层提示词，处理复杂构图和多个元素
  - **Qwen - Image Edit Combined**：综合编辑提示增强器，用于图像编辑任务
  - **Qwen - Image Dual**：专为 Qwen Image 系列（包括 Qwen Image 和 Qwen Image 2512）设计，支持高分辨率生成能力
  - **Video - Reverse Prompt**：视频反推提示词生成器，基于视频内容创建详细的视频描述（600-1000字）
  - **WAN - T2V**：电影导演风格模板，添加电影元素（时间、光源、光线强度、光线角度、色调、拍摄角度、镜头大小、构图）
  - **WAN - I2V**：视频描述提示词改写专家，强调动态内容
  - **WAN - I2V Empty**：视频描述提示词撰写专家，根据图像发挥想象生成视频描述
  - **WAN - FLF2V**：提示词优化器，基于视频首尾帧图片优化提示词，强调运动信息和镜头运镜
- 增强预设提示词分类，提升用户体验：
  - 基础模板：Empty - Nothing、Normal - Describe
  - Prompt 风格模板：Tags、Simple、Detailed、Comprehensive Expansion、Refine & Expand Prompt
  - 创意模板：Detailed Analysis、Summarize Video、Short Story
  - 视觉模板：Bounding Box
  - 专业模型模板：ZIMAGE - Turbo、FLUX2 - Klein、LTX-2、Qwen - Image Layered、Qwen - Image Edit Combined、Qwen - Image Dual
  - 视频模板：Video - Reverse Prompt
  - 电影风格模板：WAN - T2V、WAN - I2V、WAN - I2V Empty、WAN - FLF2V
- 优化了中英切换功能 
- 同步更新 README 和 Parameter-Explanation-and-Recommended-Settings 文档，包含完整的模板描述
- 提供了双语言预设模板，更好的兼容适配不同语言模型的使用（专属预设做了字数限制，满足模型生成需求的同时，保证生成结果的高效，若无法满足需求，请在预设框内输入或外挂自定义）
- 新增了生成结果的中英切换功能（部分预设添加了强制输出中文如wan等预设模板，可能会有冲突）
- 添加了汉化文件

#### 2026-01-24
- 重构了节点文件目录
- 新增了参数推荐设置文档，方便用户理解各参数对生成结果的影响
- 添加了对MiniCPM-V-4.5，LFM2.5-VL-1.6B，GLM-4.6V模型的支持类型
- 添加了中英切换功能，方便反推模型的不同类型切换
- 加载模型只支持.gguf, .safetensors格式的模型文件
- 添加了CPU/GPU运行模式选择功能：
  - 用户可以自由选择使用CPU或GPU运行模型
  - CPU模式会自动忽略GPU相关参数，强制使用纯CPU运行
  - GPU模式会根据用户设置的n_gpu_layers和vram_limit参数进行优化
  - 低性能硬件（<8GB显存）默认使用CPU模式
  - 高性能硬件（8GB+显存）默认使用GPU模式
- 性能优化：
  - 添加了语言检测结果缓存，避免重复检测
  - 添加了硬件性能参数缓存，避免重复计算
  - 优化了显存估算逻辑，仅在GPU模式下执行
  - 提高了模型加载和推理效率

#### 2026-01-17
- 添加了对llama-joycaption反推模型的支持类型
- 添加了mmproj模型开关，为了支持纯文本生成
- 添加了清理会话节点（释放当前对话占用的资源，减少不出结果的情况）
- 添加了卸载模型节点（减少显存占用）
- 添加了硬件优化模块，适配高低不同性能硬件，提高推理速度，确保不同硬件都能流畅使用
- 重写了Prompt Style预设信息

## 模型下载地址

### 常用模型下载

#### 反推模型
- **llama-joycaption**：https://huggingface.co/mradermacher/llama-joycaption-beta-one-hf-llava-GGUF
  - 推荐：llama-joycaption-beta-one-hf-llava.Q4_K_M.gguf
- **mmproj模型**：https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf
  - 推荐：llama-joycaption-beta-one-llava-mmproj-model-f16.gguf

- **MobileVLM**: https://huggingface.co/Blombert/MobileVLM-3B-GGUF
- **TinyLLaVA**: 
- **MiniGPT-v2**:
- **nanoLLaVA**: https://huggingface.co/saiphyohein/nanollava-1.5-gguf
- **LFM2.5-VL-1.6B**: https://huggingface.co/unsloth/LFM2.5-VL-1.6B-GGUF
- **Moondream2**: https://huggingface.co/Hahasb/moondream2-20250414-GGUF
- **Qwen3-VL**: https://huggingface.co/mradermacher/Qwen3-VL-8B-Instruct-abliterated-v2.0-GGUF
- **GLM-4.6V**: https://huggingface.co/unsloth/GLM-4.6V-Flash-GGUF
- **MiniCPM-V-4.5**: https://huggingface.co/openbmb/MiniCPM-V-4_5-gguf

### 量化级别选择

- **Q4_K_M**：平衡大小和质量（推荐）
- **Q5_K_M**：更高质量，稍大文件
- **Q3_K_M**：更小文件，适合低显存设备
- **Q2_K**：最小文件，质量较低

## 安装说明

### 1. 基本安装

1. **克隆或下载插件**：
   - 将插件文件夹放入 `ComfyUI/custom_nodes/` 目录
   - 文件夹名称应为 `ComfyUI-llama-cpp-vlmforQo`

2. **安装依赖**：
   ```bash
   # 在ComfyUI根目录运行
   pip install -r custom_nodes/ComfyUI-llama-cpp-vlmforQo/requirements.txt
   ```


### 2. 模型准备

1. **创建模型目录**：
   - 在 `ComfyUI/models/` 目录下创建 `LLM` 文件夹
   - 将下载的模型文件放入此目录

2. **模型文件格式**：
   - 支持 `.gguf` 和 `.safetensors` 格式
   - 视觉模型需要对应的 `mmproj` 文件

## 使用指南（根据自己电脑配置情况选择调整）

### 1. 基本使用流程

1. **加载模型**：
   - 使用 `Llama-cpp 模型加载` 节点
   - 选择模型文件和对应的 chat_handler
   - 选择运行模式（CPU 或 GPU）
   - 启用 mmproj 处理图片输入

2. **配置推理参数**：
   - 使用 `Llama-cpp 参数设置` 节点（可选）
   - 调整 temperature、max_tokens 等参数

3. **执行推理**：
   - 使用 `Llama-cpp 图片推理` 节点
   - 选择输入类型（文本、图片、视频）
   - 选择适合的提示词模板

4. **管理资源**：
   - 使用 `Llama-cpp 清理会话` 节点释放会话资源
   - 使用 `Llama-cpp 卸载模型` 节点释放模型资源

### 1.1 CPU/GPU 运行模式选择

插件支持灵活的 CPU 和 GPU 运行模式选择，用户可以根据硬件配置和需求自由选择：

#### GPU 模式（推荐）
- **适用场景**：有可用 GPU 显存的情况
- **特点**：
  - 推理速度快，适合实时应用
  - 支持更大的模型和更长的上下文
  - 自动进行显存估算和优化
- **参数设置**：
  - `n_gpu_layers`：控制加载到 GPU 的模型层数，-1 表示全部加载
  - `vram_limit`：显存限制（GB），-1 表示无限制
- **推荐配置**：
  - 24GB+ 显存：n_gpu_layers = -1, vram_limit = 24
  - 16GB 显存：n_gpu_layers = -1, vram_limit = 16
  - 12GB 显存：n_gpu_layers = -1, vram_limit = 12
  - 8GB 显存：n_gpu_layers = 30, vram_limit = 8

#### CPU 模式
- **适用场景**：
  - 无 GPU 或 GPU 显存不足
  - 需要使用 CPU 进行推理
  - 低性能硬件（<8GB 显存）
- **特点**：
  - 不依赖 GPU 显存
  - 自动忽略 GPU 相关参数
  - 推理速度较慢，但兼容性好
- **参数设置**：
  - CPU 模式下，n_gpu_layers 和 vram_limit 参数会被自动忽略
  - 无需手动调整这些参数
- **推荐配置**：
  - 适用于所有硬件配置
  - 适合小型模型和简单任务

#### 智能默认值
插件会根据硬件性能自动选择合适的运行模式：
- **高性能硬件**（8GB+ 显存）：默认使用 GPU 模式
- **低性能硬件**（<8GB 显存）：默认使用 CPU 模式
- **无 GPU 检测**：默认使用 CPU 模式

#### 使用建议
- **优先使用 GPU 模式**：如果 GPU 显存充足，优先选择 GPU 模式以获得更好的性能
- **显存不足时切换 CPU**：如果遇到显存不足错误，可以尝试切换到 CPU 模式
- **灵活切换**：可以根据任务需求随时切换运行模式
- **监控性能**：使用 GPU 模式时，注意监控显存使用情况

### 2. 推荐工作流

#### 图片描述工作流
1. 加载模型（如 Moondream2）
2. 连接图片输入
3. 选择 "Normal - Describe" 预设
4. 执行推理获取描述

#### 视频分析工作流
1. 加载模型（如 LLaVA-1.6）
2. 连接视频输入
3. 选择 "Creative - Summarize Video" 预设
4. 配置 max_frames 参数
5. 执行推理获取视频摘要

#### 边界框生成工作流
1. 加载模型（如 Qwen3-VL）
2. 连接图片输入
3. 选择 "Vision - Bounding Box" 预设
4. 使用 `JSON 转 Bounding Box` 节点可视化结果

## 常见问题

### 1. 模型加载失败

**原因**：
- 模型文件不存在或路径错误
- llama-cpp-python 版本过低
- 缺少对应的 mmproj 文件

**解决方案**：
- 检查模型文件路径
- 更新 llama-cpp-python 到最新版本
- 确保 mmproj 文件与模型匹配

### 2. 显存不足 (OOM)

**原因**：
- 模型太大，超过显存容量
- 上下文长度设置过大
- 同时运行多个大型模型

**解决方案**：
- 降低 `n_gpu_layers` 值
- 减少 `n_ctx` 值
- 使用更小的模型
- 降低图片 `max_size` 值

### 3. 推理速度慢

**原因**：
- 模型太大
- GPU 层数设置过低
- 硬件性能限制

**解决方案**：
- 使用更小的模型
- 增加 `n_gpu_layers` 值
- 降低 `n_ctx` 值
- 关闭不必要的应用程序

### 4. 生成结果质量差

**原因**：
- 模型选择不当
- 提示词质量差
- 参数设置不合理

**解决方案**：
- 使用更适合任务的模型
- 优化提示词，提供更详细的指令
- 调整 temperature、top_p 等参数
- 使用适合的提示词模板

## 高级设置

### 1. 硬件检测优化

插件会自动检测硬件性能并推荐最佳参数：
- **24GB+显存**：高性能模式，全部加载到GPU
- **16GB显存**：平衡模式，全部加载到GPU
- **12GB显存**：标准模式，全部加载到GPU
- **8GB显存**：轻量模式，部分加载到GPU
- **4-6GB显存**：兼容模式，使用CPU

### 2. 自定义参数

对于高级用户，可以手动调整以下关键参数：

- **n_ctx**：上下文长度，影响可处理的文本长度
- **n_gpu_layers**：GPU加载层数，-1=全部加载
- **temperature**：生成温度，控制随机性
- **top_p/top_k**：控制生成的多样性和准确性

## 提示词模板说明

插件内置多种提示词模板，适合不同场景：

### 基础模板
- **Empty - Nothing**：空模板，完全自定义
- **Normal - Describe**：简单描述图片内容

### Prompt 风格模板
- **Prompt Style - Tags**：生成图片标签列表，适用于SDXL等模型
- **Prompt Style - Simple**：简洁的图片描述（300字以内）
- **Prompt Style - Detailed**：详细的图片描述（500字以内）
- **Prompt Style - Comprehensive Expansion**：详细扩写提示词，增强清晰度和表现力（800字以内）
- **Creative - Refine & Expand Prompt**：优化并扩写提示词，使其更具表现力和视觉丰富性

### 创意模板
- **Creative - Detailed Analysis**：详细分析图片内容，分解主体、服装、配饰、背景和构图
- **Creative - Summarize Video**：总结视频内容的关键事件和叙事点
- **Creative - Short Story**：基于图片或视频生成短篇故事

### 视觉模板
- **Vision - *Bounding Box**：生成物体检测的边界框

### 专业模型模板
- **ZIMAGE - Turbo**：专为 Z-Image-Turbo 模型设计，创建高效且高质量的图像生成提示，利用8步Turbo推理快速生成1080P高清图像
- **FLUX2 - Klein**：专为 FLUX 系列（Flux.1 和 FLUX.2 Klein）模型设计，创建简洁而富有表现力的提示
- **LTX-2**：专为 LTX-2 模型设计，创建详细而富有动态感的视频生成提示，支持高质量、音画同步的4K视频
- **Qwen - Image Layered**：专为 Qwen-Image-Layered 模型设计，创建详细的分层提示，处理复杂构图和多个元素
- **Qwen - Image Edit Combined**：综合编辑提示增强器，用于图像编辑任务
- **Qwen - Image Dual**：专为 Qwen Image 系列（包括 Qwen Image 和 Qwen Image 2512）模型设计，创建高质量的图像生成提示

### 视频模板
- **Video - Reverse Prompt**：视频反推提示词，根据视频内容生成详细的视频描述提示词（600-1000字）

### 电影风格模板
- **WAN - T2V**：电影导演风格，为原始prompt添加电影元素（时间、光源、光线强度、光线角度、色调、拍摄角度、镜头大小、构图等）
- **WAN - I2V**：视频描述提示词改写专家，根据图像和输入提示词改写视频描述，强调动态内容（120-150字）
- **WAN - I2V Empty**：视频描述提示词撰写专家，根据图像发挥想象生成视频描述（120-150字）
- **WAN - FLF2V**：Prompt优化师，根据视频首尾帧图片优化改写Prompt，强调运动信息和镜头运镜
## 致谢
* [ComfyUI-llama-cpp_vlm](https://github.com/lihaoyun6/ComfyUI-llama-cpp_vlm) @lihaoyun6
* [llama-cpp-python](https://github.com/JamePeng/llama-cpp-python) @JamePeng
* [ComfyUI-llama-cpp](https://github.com/kijai/ComfyUI-llama-cpp) @kijai
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI) @comfyanonymous
