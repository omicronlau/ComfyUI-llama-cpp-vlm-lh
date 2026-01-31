# ComfyUI-llama-cpp-vlmforQo  
Run LLM/VLM models natively in ComfyUI based on llama.cpp, supporting multimodal inference, visual language understanding, and various AI tasks.  
**[[📃中文版](./README_zh.md)]**

## Project Introduction

ComfyUI-llama-cpp-vlmforQo is a powerful ComfyUI plugin that allows users to run various large language models (LLM) and vision language models (VLM) locally without relying on cloud services. Based on llama.cpp technology, this plugin provides efficient model inference capabilities, supporting a wide range of devices from high-end to low-end GPUs.

### Project Goals
- Enable local execution of advanced AI models without cloud dependency
- Provide seamless integration of multimodal capabilities into ComfyUI workflows
- Optimize performance across different hardware configurations
- Support a wide variety of popular LLM and VLM models
- Offer flexible parameter control for fine-tuning model behavior

### Key Advantages
- **Privacy-First**: All processing happens locally, no data sent to cloud servers
- **Cost-Effective**: No API fees or subscription costs
- **Versatile**: Supports both text-only and multimodal models
- **Hardware-Aware**: Automatically optimizes settings based on available resources
- **Extensible**: Easy to integrate with other ComfyUI nodes and workflows

## Core Features

- **Multimodal Support**: Process text, image, and video inputs
- **Wide Model Compatibility**: Support for 20+ mainstream VLM/LLM models
- **Intelligent Hardware Adaptation**: Automatically adjust parameters based on VRAM size
- **Efficient Inference**: Optimized model loading and inference workflow
- **Rich Preset Templates**: Built-in multiple prompt templates
- **Flexible Parameter Control**: Detailed inference parameter settings
- **Session Management**: Support for session state saving and cleaning

## Chinese Translation

Place the zh-CN files into the corresponding folder of the translation plugin (ComfyUI-Chinese-Translation/AIGODLIKE-ComfyUI-Translation/ComfyUI-DD-Translation) to override. It is recommended to install the ComfyUI-Chinese-Translation plugin for more comprehensive localization and faster translation updates.

## Supported Models

### Static Supported Models
- "LLaVA-1.5", "LLaVA-1.6", "Moondream2", "nanoLLaVA"
- "llama3-Vision-Alpha", "MiniCPM-v2.6", "MiniCPM-v4", "MiniCPM-V-4.5"
- "LFM2.5-VL", "GLM-4.6V", "llama-joycaption"

### Dynamically Imported Models (depending on llama-cpp-python version)
- "Gemma3", "Qwen2.5-VL", "Qwen3-VL", "Qwen3-VL-Chat", "Qwen3-VL-Instruct"
- "GLM-4.1V-Thinking", "LFM2-VL", "MobileVLM", "TinyLLaVA", "MiniGPT-v2"

- The plugin already supports LFM2.5-VL model loading, but llama_cpp_python is not yet compatible

## Hardware Requirements

### Recommended Configuration Based on VRAM Size

#### 24GB+ VRAM (e.g., 5090, 4090, 3090)
- **Recommended Models**: Any model, including the largest vision language models
- **Performance**: Smoothly run all models, support maximum context length

#### 16GB VRAM (e.g., 4080)
- **Recommended Models**: LLaVA-1.6, MiniCPM-V-4.5, Qwen2.5-VL, LFM2.5-VL
- **Performance**: Balance between performance and quality

#### 12GB VRAM (e.g., 4070 Ti, 3080)
- **Recommended Models**: LLaVA-1.5, MiniCPM-v2.6, Moondream2, LFM2.5-VL
- **Performance**: Suitable for most tasks

#### 8GB VRAM (e.g., 3070, 3060)
- **Recommended Models**: Moondream2, nanoLLaVA, LFM2.5-VL-1.6B, MobileVLM, TinyLLaVA
- **Performance**: Suitable for basic visual understanding tasks

#### 4-6GB VRAM
- **Recommended Models**: nanoLLaVA, TinyLLaVA, MiniGPT-v2
- **Performance**: May require CPU-only operation, suitable for simple tasks

## Changelog
#### 2026-01-29
- Restructured file directory, please delete old version files when installing, do not overwrite
- Added comprehensive preset prompt templates for specialized AI models:
  - **ZIMAGE - Turbo**: Optimized for Z-Image-Turbo model with 8-step Turbo inference for rapid 1080P HD image generation
  - **FLUX2 - Klein**: Designed for FLUX series (Flux.1 and FLUX.2 Klein) models with concise and expressive prompts
  - **LTX-2**: Specialized for LTX-2 video generation model with dynamic video prompts supporting 4K audio-visual synchronized output
  - **Qwen - Image Layered**: Created for Qwen-Image-Layered model with detailed layered prompts for complex compositions
  - **Qwen - Image Edit Combined**: Comprehensive editing prompt enhancer for image editing tasks
  - **Qwen - Image Dual**: Designed for Qwen Image series (including Qwen Image and Qwen Image 2512) with high-resolution generation capabilities
  - **Video - Reverse Prompt**: Video reverse prompt generator for creating detailed video descriptions (600-1000 words) based on video content
  - **WAN - T2V**: Cinematic director style template adding cinematic elements (time, light source, light intensity, light angle, color tone, shooting angle, lens size, composition)
  - **WAN - I2V**: Video description prompt rewriting expert emphasizing dynamic content 
  - **WAN - I2V Empty**: Video description prompt writing expert generating video descriptions from images with imagination 
  - **WAN - FLF2V**: Prompt optimizer optimizing prompts based on video first and last frame images, emphasizing motion information and camera movement
- Enhanced preset prompt categorization for better user experience:
  - Basic templates: Empty - Nothing, Normal - Describe
  - Prompt Style templates: Tags, Simple, Detailed, Comprehensive Expansion, Refine & Expand Prompt
  - Creative templates: Detailed Analysis, Summarize Video, Short Story
  - Vision templates: Bounding Box
  - Professional Model templates: ZIMAGE - Turbo, FLUX2 - Klein, LTX-2, Qwen - Image Layered, Qwen - Image Edit Combined, Qwen - Image Dual
  - Video templates: Video - Reverse Prompt
  - Cinematic Style templates: WAN - T2V, WAN - I2V, WAN - I2V Empty, WAN - FLF2V
- Optimized Chinese-English switching function
- Synchronized README and Parameter-Explanation-and-Recommended-Settings documentation with complete template descriptions
- Provided bilingual preset templates for better compatibility with different language models (exclusive presets have word count limits to meet model generation needs while ensuring efficient results, if they cannot meet requirements, please input in the preset box or use external custom presets)
- Added Chinese-English switching function for generated results (some presets like wan have forced Chinese output, which may cause conflicts)
- Added localization files

#### 2026-01-24
- Restructured node file directory
- Added parameter recommendation settings documentation for users to understand the impact of each parameter on generation results
- Added support for MiniCPM-V-4.5, LFM2.5-VL-1.6B, GLM-4.6V models
- Added Chinese-English switching function for reverse models
- Only support .gguf and .safetensors format model files
- Added CPU/GPU runtime mode selection feature:
  - Users can freely choose to run models using CPU or GPU
  - CPU mode automatically ignores GPU-related parameters and forces pure CPU execution
  - GPU mode optimizes based on user-set n_gpu_layers and vram_limit parameters
  - Low-performance hardware (<8GB VRAM) defaults to CPU mode
  - High-performance hardware (8GB+ VRAM) defaults to GPU mode
- Performance optimizations:
  - Added language detection result caching to avoid repeated detection
  - Added hardware performance parameter caching to avoid repeated calculations
  - Optimized VRAM estimation logic, only executed in GPU mode
  - Improved model loading and inference efficiency

#### 2026-01-17  
- Added support for llama-joycaption reverse model, personal recommendation: Qwen3VL unrestricted model
- Added mmproj model switch to support pure text generation
- Added clean session node (releases resources occupied by current conversation, reduces cases of no results)
- Added unload model node (reduces VRAM usage)
- Added hardware optimization module to adapt to different performance hardware, improve inference speed, and ensure smooth usage on different hardware
- Rewrote Prompt Style preset information

## Model Downloads

### Common Model Downloads

#### Reverse Models
- **llama-joycaption**: https://huggingface.co/mradermacher/llama-joycaption-beta-one-hf-llava-GGUF
  - Recommended: llama-joycaption-beta-one-hf-llava.Q4_K_M.gguf
- **mmproj model**: https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf
  - Recommended: llama-joycaption-beta-one-llava-mmproj-model-f16.gguf

- **MobileVLM**: https://huggingface.co/Blombert/MobileVLM-3B-GGUF
- **nanoLLaVA**: https://huggingface.co/saiphyohein/nanollava-1.5-gguf
- **LFM2.5-VL-1.6B**: https://huggingface.co/unsloth/LFM2.5-VL-1.6B-GGUF
- **Moondream2**: https://huggingface.co/Hahasb/moondream2-20250414-GGUF
- **Qwen3-VL**: https://huggingface.co/mradermacher/Qwen3-VL-8B-Instruct-abliterated-v2.0-GGUF
- **GLM-4.6V**: https://huggingface.co/unsloth/GLM-4.6V-Flash-GGUF
- **MiniCPM-V-4.5**: https://huggingface.co/openbmb/MiniCPM-V-4_5-gguf

### Quantization Level Selection

- **Q4_K_M**: Balanced size and quality (recommended)
- **Q5_K_M**: Higher quality, slightly larger file
- **Q3_K_M**: Smaller file, suitable for low VRAM devices
- **Q2_K**: Smallest file, lower quality

## Preview  
![](./img/preview.jpg)

## Installation Instructions

### 1. Basic Installation

1. **Clone or download the plugin**:
   - Place the plugin folder into `ComfyUI/custom_nodes/` directory
   - The folder name should be `ComfyUI-llama-cpp-vlmforQo`

2. **Install dependencies**:
   ```bash
   # Run in ComfyUI root directory
   pip install -r custom_nodes/ComfyUI-llama-cpp-vlmforQo/requirements.txt
   ```

### 2. Model Preparation

1. **Create model directory**:
   - Create `LLM` folder in `ComfyUI/models/` directory
   - Place downloaded model files into this directory

2. **Model file formats**:
   - Supports `.gguf` and `.safetensors` formats
   - Vision models require corresponding `mmproj` files

## Workflow Examples

[workflow](./workflow/llama-cpp-vlmforQo.json)

![workflow](./workflow/TEXT.png)

![workflow](./workflow/Images.png)

## Usage Guide (Adjust according to your computer configuration)

### 1. Basic Usage Flow

1. **Load Model**:
   - Use the `Llama-cpp Model Loader` node
   - Select model file and corresponding chat_handler
   - Choose runtime mode (CPU or GPU)
   - Enable mmproj to process image input

2. **Configure Inference Parameters**:
   - Use the `Llama-cpp Parameter Settings` node (optional)
   - Adjust temperature, max_tokens and other parameters

3. **Execute Inference**:
   - Use the `Llama-cpp Image Inference` node
   - Select input type (text, image, video)
   - Choose appropriate prompt template

4. **Manage Resources**:
   - Use the `Llama-cpp Clean Session` node to release session resources
   - Use the `Llama-cpp Unload Model` node to release model resources

### 1.1 CPU/GPU Runtime Mode Selection

The plugin supports flexible CPU and GPU runtime mode selection, allowing users to freely choose based on hardware configuration and needs:

#### GPU Mode (Recommended)
- **Applicable Scenarios**: When GPU VRAM is available
- **Features**:
  - Fast inference speed, suitable for real-time applications
  - Supports larger models and longer contexts
  - Automatic VRAM estimation and optimization
- **Parameter Settings**:
  - `n_gpu_layers`: Controls the number of model layers loaded to GPU, -1 means load all
  - `vram_limit`: VRAM limit (GB), -1 means no limit
- **Recommended Configuration**:
  - 24GB+ VRAM: n_gpu_layers = -1, vram_limit = 24
  - 16GB VRAM: n_gpu_layers = -1, vram_limit = 16
  - 12GB VRAM: n_gpu_layers = -1, vram_limit = 12
  - 8GB VRAM: n_gpu_layers = 30, vram_limit = 8

#### CPU Mode
- **Applicable Scenarios**:
  - No GPU or insufficient GPU VRAM
  - Need to use CPU for inference
  - Low-performance hardware (<8GB VRAM)
- **Features**:
  - Does not depend on GPU VRAM
  - Automatically ignores GPU-related parameters
  - Slower inference speed, but good compatibility
- **Parameter Settings**:
  - In CPU mode, n_gpu_layers and vram_limit parameters are automatically ignored
  - No need to manually adjust these parameters
- **Recommended Configuration**:
  - Suitable for all hardware configurations
  - Suitable for small models and simple tasks

#### Smart Defaults
The plugin automatically selects appropriate runtime mode based on hardware performance:
- **High-performance hardware** (8GB+ VRAM): Defaults to GPU mode
- **Low-performance hardware** (<8GB VRAM): Defaults to CPU mode
- **No GPU detected**: Defaults to CPU mode

#### Usage Recommendations
- **Prioritize GPU mode**: If GPU VRAM is sufficient, prioritize GPU mode for better performance
- **Switch to CPU when VRAM is insufficient**: If you encounter OOM errors, try switching to CPU mode
- **Flexible switching**: You can switch runtime modes anytime based on task requirements
- **Monitor performance**: When using GPU mode, monitor VRAM usage

### 2. Recommended Workflows

#### Image Description Workflow
1. Load model (e.g., Moondream2)
2. Connect image input
3. Select "Normal - Describe" preset
4. Execute inference to get description

#### Video Analysis Workflow
1. Load model (e.g., LLaVA-1.6)
2. Connect video input
3. Select "Creative - Summarize Video" preset
4. Configure max_frames parameter
5. Execute inference to get video summary

#### Bounding Box Generation Workflow
1. Load model (e.g., Qwen3-VL)
2. Connect image input
3. Select "Vision - Bounding Box" preset
4. Use `JSON to Bounding Box` node to visualize results

## Common Questions

### 1. Model Loading Issues

**Reasons**:
- Model file doesn't exist or path is incorrect
- llama-cpp-python version is too low
- Missing corresponding mmproj file

**Solutions**:
- Check model file path
- Update llama-cpp-python to the latest version
- Ensure mmproj file matches the model

### 2. Out of Memory (OOM) Issues

**Reasons**:
- Model is too large, exceeding VRAM capacity
- Context length is set too large
- Multiple large models running simultaneously

**Solutions**:
- Reduce `n_gpu_layers` value
- Decrease `n_ctx` value
- Use a smaller model
- Try CPU mode if GPU memory is insufficient
- Lower image `max_size` for VLM tasks

### 3. Slow Inference Speed

**Reasons**:
- Model is too large
- GPU layers setting is too low
- Hardware performance limitations

**Solutions**:
- Use a smaller model
- Increase `n_gpu_layers` value
- Reduce `n_ctx` value
- Close unnecessary applications

### 4. Poor Generation Quality

**Reasons**:
- Inappropriate model selection
- Poor prompt quality
- Unreasonable parameter settings

**Solutions**:
- Use a more suitable model for the task
- Optimize prompts with more detailed instructions
- Adjust temperature, top_p, and other parameters
- Use appropriate prompt templates

## Advanced Settings

### 1. Hardware Detection Optimization

The plugin automatically detects hardware performance and recommends optimal parameters:
- **24GB+ VRAM**: High-performance mode, full GPU loading
- **16GB VRAM**: Balanced mode, full GPU loading
- **12GB VRAM**: Standard mode, full GPU loading
- **8GB VRAM**: Lightweight mode, partial GPU loading
- **4-6GB VRAM**: Compatible mode, using CPU

### 2. Custom Parameters

For advanced users, you can manually adjust the following key parameters:

- **n_ctx**: Context length, affects the length of text that can be processed
- **n_gpu_layers**: GPU loading layers, -1=load all
- **temperature**: Generation temperature, controls randomness
- **top_p/top_k**: Control the diversity and accuracy of generation

## Prompt Template Instructions

The plugin includes various prompt templates for different scenarios:

### Basic Templates
- **Empty - Nothing**: Empty template, fully customizable
- **Normal - Describe**: Simply describe image content

### Prompt Style Templates
- **Prompt Style - Tags**: Generate image tag lists, suitable for models like SDXL
- **Prompt Style - Simple**: Concise image description (within 300 words)
- **Prompt Style - Detailed**: Detailed image description (within 500 words)
- **Prompt Style - Comprehensive Expansion**: Detailed prompt expansion, enhancing clarity and expressiveness (within 800 words)
- **Creative - Refine & Expand Prompt**: Optimize and expand prompts to make them more expressive and visually rich

### Creative Templates
- **Creative - Detailed Analysis**: Detailed analysis of image content, breaking down subject, clothing, accessories, background, and composition
- **Creative - Summarize Video**: Summarize key events and narrative points of video content
- **Creative - Short Story**: Generate short stories based on images or videos

### Vision Templates
- **Vision - Bounding Box**: Generate object detection bounding boxes

### Professional Model Templates
- **ZIMAGE - Turbo**: Designed for Z-Image-Turbo model, creating efficient and high-quality image generation prompts, using 8-step Turbo inference for rapid 1080P HD image generation
- **FLUX2 - Klein**: Designed for FLUX series (Flux.1 and FLUX.2 Klein) models, creating concise and expressive prompts
- **LTX-2**: Designed for LTX-2 model, creating detailed and dynamic video generation prompts, supporting high-quality, audio-visual synchronized 4K video
- **Qwen - Image Layered**: Designed for Qwen-Image-Layered model, creating detailed layered prompts for complex compositions
- **Qwen - Image Edit Combined**: Comprehensive editing prompt enhancer for image editing tasks
- **Qwen - Image Dual**: Designed for Qwen Image series (including Qwen Image and Qwen Image 2512) models, creating high-quality image generation prompts

### Video Templates
- **Video - Reverse Prompt**: Video reverse prompt, generating detailed video description prompts based on video content

### Cinematic Style Templates
- **WAN - T2V**: Cinematic director style, adding cinematic elements (time, light source, light intensity, light angle, color tone, shooting angle, lens size, composition, etc.) to original prompts
- **WAN - I2V**: Video description prompt rewriting expert, rewriting video descriptions based on images and input prompts, emphasizing dynamic content
- **WAN - I2V Empty**: Video description prompt writing expert, generating video descriptions from images with imagination
- **WAN - FLF2V**: Prompt optimizer, optimizing and rewriting prompts based on video first and last frame images, emphasizing motion information and camera movement

## Credits  
- [ComfyUI-llama-cpp_vlm](https://github.com/lihaoyun6/ComfyUI-llama-cpp_vlm) @lihaoyun6
- [llama-cpp-python](https://github.com/JamePeng/llama-cpp-python) @JamePeng  
- [ComfyUI-llama-cpp](https://github.com/kijai/ComfyUI-llama-cpp) @kijai  
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) @comfyanonymous
