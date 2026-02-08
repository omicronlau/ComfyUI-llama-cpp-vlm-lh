# ComfyUI-llama-cpp-vlmforQo

Run LLM/VLM models natively in ComfyUI based on llama.cpp, supporting multimodal inference, visual language understanding, and various AI tasks.

**[📃中文版](./README_zh.md)**

## Project Introduction

ComfyUI-llama-cpp-vlmforQo is a comprehensive and performance-optimized ComfyUI plugin, deeply refactored and enhanced based on the ComfyUI-llama-cpp-vlm plugin, focusing on providing localized, efficient multimodal AI inference capabilities.

Compared to similar plugins, this project has achieved significant breakthroughs in the following aspects:
- **More comprehensive multimodal support**: Not only supports text and images, but also adds video input and analysis capabilities
- **Smarter hardware adaptation**: Based on llama.cpp technology, implements intelligent parameter tuning from high-end to low-end devices
- **Rich model ecosystem**: Supports multiple mainstream VLM/LLM models, including the latest professional AI models, with dynamic support functionality—when llama_cpp_python updates and supports new model versions, users can directly download and use them without modifying plugin code
- **Optimized inference performance**: Reconstructs model loading and inference processes, significantly improving operational efficiency
- **Professional prompt system**: Built-in rich preset templates covering full-scenario needs from basic description to professional model optimization

> Note: Incompatible with ComfyUI-llama-cpp-vlm and branch plugins

## Core Features

- **Multimodal Full Support**: Process text, image, and video inputs, enabling cross-modal understanding and generation
- **Wide Model Compatibility**: Support for multiple mainstream VLM/LLM models, including the latest professional AI models, with dynamic support functionality—when llama_cpp_python updates and supports new model versions, users can directly download and use them without modifying plugin code
- **Intelligent Hardware Adaptation**: Automatically adjust parameters based on VRAM size to maximize hardware performance
- **Efficient Inference Engine**: Optimized model loading and inference workflow, significantly improving operational speed
- **Professional Prompt System**: Built-in rich preset templates covering full-scenario needs from basic description to professional model optimization
- **Flexible Parameter Control**: Detailed inference parameter settings to meet customized needs for different scenarios

- **Video Processing Capability**: Added video input support, enabling video content analysis and reverse generation
- **CPU/GPU Mode**: Freely switch between runtime modes to adapt to different hardware configurations
- **Hardware Detection Optimization**: Automatically detect hardware performance and recommend optimal parameter configurations


## Chinese Translation

Place the zh-CN files into the corresponding folder of the translation plugin (ComfyUI-Chinese-Translation/AIGODLIKE-ComfyUI-Translation/ComfyUI-DD-Translation) to override. It is recommended to install the ComfyUI-Chinese-Translation plugin for more comprehensive localization and faster translation updates.

## Supported Models

- LLaVA-1.6
- nanoLLaVA
- MiniCPM-V-4.5
- GLM-4.6V
- llama-joycaption
- moondream3-preview
- Moondream2
- InternLM-XComposer2-VL
- DreamOmni2
- MiniCPM-Llama3-V 2.5
- Llama-3.2-11B-Vision-Instruct
- CogVLM2
- CogVLM-MOE
- Phi-3.5-vision-instruct
- Phi-3-vision-128k-instruct
- Qwen2.5-VL
- Qwen3-VL
- Qwen3-VL-Chat
- Qwen3-VL-Instruct
- LLaMA-3.1-Vision
- Zhipu-Vision
- ZhiPu AI-Vision
- olmOCR-2
- InternVL-1.5
- InternVL-2.0
- Yi-VL-2.0

> Note: The plugin already supports multiple model loading, specific support depends on llama_cpp_python version



## Changelog
#### 2026-02-05
- Added multiple new preset prompt templates: Bilingual Prompt Generate, Ultra HD Image Reverse
- Optimized model loading and inference workflow for improved efficiency
- Enhanced Chinese localization support
- Added video interface support, enabling video input and introducing new templates for video reverse functionality:
  - Video Scene Breakdown Preset: Automatically generates scene-by-scene prompts based on video content
  - Video Subtitle Preset: Automatically generates subtitle prompts based on video content
- Added OCR enhancement functionality, supporting poster text recognition and style restoration, optimized for prompt reverse requirements:
  - OCR Enhancement Prompt Template: Specifically designed for poster OCR text recognition, accurately extracting text content and style attributes
  - Supports recognition of text font, size, color, typesetting style and other detailed attributes
- Implemented intelligent model detection system that automatically discovers and supports new VL models added in llama_cpp_python
- Optimized model name inference logic to automatically generate model names based on ChatHandler naming conventions
- Expanded model support list to ensure backward compatibility with all previously supported models
- Implemented model list deduplication functionality to keep the interface clean and organized
- Added support for multiple models: moondream3-preview, InternLM-XComposer2-VL, DreamOmni2, MiniCPM-Llama3-V 2.5, Llama-3.2-11B-Vision-Instruct, Phi-3.5-vision-instruct, Moondream2, olmOCR-2, InternVL-1.5, InternVL-2.0, Yi-VL-2.0
- Added dynamic support functionality, when llama_cpp_python updates and releases support for new model versions, users can directly download and use the models

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
- Optimized Chinese-English switching function for better language adaptation
- Provided bilingual preset templates (English and Chinese) for better compatibility with different language models (exclusive presets have word count limits to meet model generation needs while ensuring efficient results, if they cannot meet requirements, please input in the preset box or use external custom presets)
- Added Chinese-English switching function for generated results

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
- **mmproj model**: https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf

#### Lightweight Models
- **MobileVLM**: https://huggingface.co/Blombert/MobileVLM-3B-GGUF
- **nanoLLaVA**: https://huggingface.co/saiphyohein/nanollava-1.5-gguf
- **Moondream2**: https://huggingface.co/Hahasb/moondream2-20250414-GGUF
- **moondream3-preview**: https://huggingface.co/vikhyatk/moondream3

#### Multimodal Models
- **Qwen3-VL**: https://huggingface.co/mradermacher/Qwen3-VL-8B-Instruct-abliterated-v2.0-GGUF
- **Qwen2.5-VL**: https://huggingface.co/Qwen/Qwen2.5-VL-2B-Instruct-GGUF
- **GLM-4.6V**: https://huggingface.co/huihui-ai/Huihui-GLM-4.6V-Flash-abliterated-GGUF
- **MiniCPM-V-4.5**: https://huggingface.co/openbmb/MiniCPM-V-4_5-gguf
- **MiniCPM-Llama3-V 2.5**: https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5
- **Phi-3.5-vision-instruct**: https://huggingface.co/microsoft/Phi-3.5-vision-instruct
- **Phi-3-vision-128k-instruct**: https://huggingface.co/microsoft/Phi-3-vision-128k-instruct
- **Llama-3.2-11B-Vision-Instruct**: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct
- **InternLM-XComposer2-VL**: https://huggingface.co/InternLM/InternLM-XComposer2-VL
- **InternVL-1.5**: https://huggingface.co/OpenGVLab/InternVL-1.5
- **InternVL-2.0**: https://huggingface.co/OpenGVLab/InternVL-2.0
- **DreamOmni2**: https://huggingface.co/DreamOmni/DreamOmni2
- **CogVLM2**: https://huggingface.co/THUDM/CogVLM2
- **CogVLM-MOE**: https://huggingface.co/THUDM/CogVLM-MOE
- **LLaMA-3.1-Vision**: https://huggingface.co/meta-llama/Llama-3.1-8B-Vision-Instruct
- **Yi-VL-2.0**: https://huggingface.co/01-ai/Yi-VL-2.0
- **olmOCR-2**: https://huggingface.co/allenai/olmOCR-2

### Quantization Level Selection

- **Q4_K_M**: Balanced size and quality (recommended)
- **Q5_K_M**: Higher quality, slightly larger file
- **Q3_K_M**: Smaller file, suitable for low VRAM devices
- **Q2_K**: Smallest file, lower quality

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

[Workflow File](./workflows/llama-cpp-vlmforQo.json)

![Workflow Example - Text Mode](./workflows/TEXT.png)

![Workflow Example - Image Mode](./workflows/Images.png)

![Workflow Example - Video Mode](./workflows/Video.png)

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
- **Prompt Style - Tags**: Generate image tag lists, suitable for models like SDXL, maximum output 50 unique tags
- **Prompt Style - Simple**: Concise image description (within 300 words), enhancing clarity and expressiveness
- **Prompt Style - Detailed**: Detailed image description (within 500 words), adding specific details for each element
- **Prompt Style - Comprehensive Expansion**: Detailed prompt expansion (within 800 words), enhancing clarity and expressiveness
- **Creative - Refine & Expand Prompt**: Optimize and expand prompts to make them more expressive and visually rich

### Creative Templates
- **Creative - Detailed Analysis**: Detailed analysis of image content, breaking down subject, clothing, accessories, background, and composition
- **Creative - Summarize Video**: Summarize key events and narrative points of video content
- **Creative - Short Story**: Generate short stories based on images or videos

### Vision Templates
- **Vision - Bounding Box**: Generate object detection bounding boxes, output JSON format coordinate list

### OCR Templates
- **OCR - Enhanced**: Professional poster OCR text recognition, accurately extracting text content and style attributes, optimized for prompt reverse requirements

### Multilingual Templates
- **[Multilingual] Bilingual Prompt Generate**: Professional bilingual prompt generation expert, specializing in creating high-quality Chinese-English bilingual prompts for cross-border creation and bilingual document scenarios, ensuring both languages convey the same visual information and creative intent

### High Resolution Templates
- **[HighRes] Ultra HD Image Reverse**: Professional ultra HD image prompt reverse expert, specializing in extracting detailed visual information from 4K/8K ultra HD images and generating accurate prompts, including all details such as subjects, scenes, materials, textures, lighting, colors, and composition

### Video Templates
- **Video - Reverse Prompt**: Video reverse prompt, generating detailed video description prompts based on video content
- **Video - Detailed Scene Breakdown**: Detailed video scene breakdown, providing complete details for each scene in chronological order
- **Video - Subtitle Format**: Generate standard format video subtitles, including time codes and synchronized text

### Professional Model Templates
- **ZIMAGE - Turbo**: Designed for Z-Image-Turbo model, creating efficient and high-quality image generation prompts, using 8-step Turbo inference for rapid 1080P HD image generation
- **FLUX2 - Klein**: Designed for FLUX series (Flux.1 and FLUX.2 Klein) models, creating concise and expressive prompts
- **LTX-2**: Designed for LTX-2 model, creating detailed and dynamic video generation prompts, supporting high-quality, audio-visual synchronized 4K video
- **Qwen - Image Layered**: Designed for Qwen-Image-Layered model, creating detailed layered prompts for complex compositions
- **Qwen - Image Edit Combined**: Comprehensive editing prompt enhancer for image editing tasks, supporting add, delete, replace and other operations
- **Qwen - Image Dual**: Designed for Qwen Image series (including Qwen Image and Qwen Image 2512) models, creating high-quality image generation prompts

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
