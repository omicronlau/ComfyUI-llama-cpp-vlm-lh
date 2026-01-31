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

- **Multimodal Support**: Process text, image, and video inputs seamlessly
  - Text-only tasks: Chat, translation, summarization, code generation
  - Image understanding: Description, object detection, scene analysis
  - Video analysis: Content summarization, action recognition

- **Wide Model Compatibility**: Support for 20+ mainstream VLM/LLM models
  - Latest vision models: Qwen3-VL, GLM-4.6V, MiniCPM-V-4_5
  - Classic models: LLaVA-1.5/1.6, Moondream2, nanoLLaVA
  - Lightweight models: MobileVLM, TinyLLaVA, MiniGPT-v2

- **Intelligent Hardware Adaptation**: Automatically adjust parameters based on VRAM size
  - Dynamic parameter optimization for different GPU configurations
  - Smart CPU/GPU mode selection based on hardware capabilities
  - Memory-efficient loading strategies for limited-resource devices

- **Efficient Inference**: Optimized model loading and inference workflow
  - Fast model initialization and loading
  - Memory management optimizations
  - Batch processing capabilities for multiple inputs

- **Rich Preset Templates**: Built-in multiple prompt templates
  - Image description templates for different detail levels
  - Video analysis templates for content summarization
  - Creative writing templates for story generation
  - Object detection templates for bounding box generation

- **Flexible Parameter Control**: Detailed inference parameter settings
  - Comprehensive control over sampling parameters (temperature, top_p, top_k)
  - Context length adjustment for handling long inputs
  - Customizable output length and formatting

- **Session Management**: Support for session state saving and cleaning
  - Persistent conversation context for coherent interactions
  - Resource management to prevent memory leaks
  - Multiple concurrent session support

## Supported Models

### Static Supported Models
- "LLaVA-1.5", "LLaVA-1.6", "Moondream2", "nanoLLaVA"
- "llama3-Vision-Alpha", "MiniCPM-v2.6", "MiniCPM-v4", "MiniCPM-V-4.5"
- "LFM2.5-VL", "GLM-4.6V", "llama-joycaption"

### Dynamically Imported Models (depending on llama-cpp-python version)
- "Gemma3", "Qwen2.5-VL", "Qwen3-VL", "Qwen3-VL-Chat", "Qwen3-VL-Instruct"
- "GLM-4.1V-Thinking", "LFM2-VL", "MobileVLM", "TinyLLaVA", "MiniGPT-v2"

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
- Synchronized README and Parameter-Explanation-and-Recommended-Settings documentation with complete template descriptions

#### 2026-01-24
- Added support for MiniCPM-V-4_5, LFM2.5-VL-1.6B, GLM-4.6V, MobileVLM, TinyLLaVA, MiniGPT-v2 models
- Added Chinese-English switching function for reverse models (not effective in text-to-image mode)
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
- Hardware detection optimization:
  - Added support for 5090 GPU recognition
  - Implemented multi-level performance classification based on VRAM size
  - Added perf_level field for more refined performance judgment
- Parameter recommendation optimization:
  - Provide more appropriate default parameters based on different performance levels
  - Recommended partial GPU layer loading for 8GB VRAM GPUs
  - Recommended smaller context length for low VRAM GPUs
- User experience improvements:
  - Automatically adjust default parameters based on hardware performance
  - Provide clearer model selection recommendations
  - Ensure smooth operation from high-end to low-end GPUs

#### 2026-01-17  
- Added support for llama-joycaption reverse model, personal recommendation: Qwen3VL unrestricted model
- Added mmproj model switch to support pure text generation
- Added clean session node (releases resources occupied by current conversation, reduces cases of no results)
- Added unload model node (reduces VRAM usage)
- Added hardware optimization module to adapt to different performance hardware, improve inference speed, and ensure smooth usage on different hardware
- Rewrote Prompt Style preset information

## Model Downloads  
- **llama-joycaption model**: [Hugging Face Link](https://huggingface.co/mradermacher/llama-joycaption-beta-one-hf-llava-GGUF/tree/main)  
  - Select a quantization model package suitable for your computer's GPU (e.g., llama-joycaption-beta-one-hf-llava.Q4_K_M.gguf)
- **mmproj model**: [Hugging Face Link](https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf/tree/main)  
  - Download: llama-joycaption-beta-one-llava-mmproj-model-f16.gguf
- **Qwen3VL unrestricted model**: [Hugging Face Link](https://huggingface.co/mradermacher/Qwen3-VL-8B-Instruct-abliterated-v2.0-GGUF/tree/main)

## Preview  
![](./img/preview.jpg)

## Installation  

### Install the node

#### Method 1: Using Git (Recommended)
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/lihaoyun6/ComfyUI-llama-cpp-vlmforQo.git
python -m pip install -r ComfyUI-llama-cpp-vlmforQo/requirements.txt
```

#### Method 2: Manual Installation
1. Download the repository as a ZIP file
2. Extract it to `ComfyUI/custom_nodes/ComfyUI-llama-cpp-vlmforQo`
3. Run:
   ```bash
   python -m pip install -r ComfyUI/custom_nodes/ComfyUI-llama-cpp-vlmforQo/requirements.txt
   ```

### Install llama-cpp-python with GPU support

#### For NVIDIA GPUs (Recommended)
```bash
# Windows
python -m pip install llama-cpp-python --extra-index-url https://james-brennan.github.io/prebuilt-packages/

# Linux
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 python -m pip install llama-cpp-python
```

#### For CPU-only installation
```bash
python -m pip install llama-cpp-python
```

### Download models

1. **Create model directory**:
   - Create `LLM` folder in `ComfyUI/models/` if it doesn't exist

2. **Place your model files**:
   - Put your GGUF model files in `ComfyUI/models/LLM`
   - For VLM models, also download the corresponding `mmproj` files

3. **Recommended models**:
   - **General purpose**: Qwen3-VL, LLaVA-1.6
   - **Lightweight**: Moondream2, MobileVLM
   - **Image captioning**: llama-joycaption

> **Important**: If you need a VLM model to process image input, don't forget to download the matching `mmproj` weights.

## Usage Guide

### 1. Basic Workflow

1. **Load Model**:
   - Use the `Llama-cpp Model Loader` node
   - Select the model file and corresponding chat_handler
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

### 2. Advanced Usage Examples

#### Image Description Workflow
1. **Model Setup**:
   - Load Moondream2 or LLaVA-1.6 model
   - Enable mmproj for image processing
   - Set appropriate context length based on GPU memory

2. **Inference Configuration**:
   - Select "Normal - Describe" or "Prompt Style - Detailed" template
   - Set max_tokens to 768-1024 for detailed descriptions
   - Adjust temperature to 0.7 for balanced creativity

3. **Processing**:
   - Connect image input to the inference node
   - Execute workflow to get detailed image description

#### Video Analysis Workflow
1. **Model Setup**:
   - Load LLaVA-1.6 or Qwen3-VL model (recommended for video)
   - Enable GPU mode if available
   - Set n_ctx to 8192 or higher

2. **Inference Configuration**:
   - Select "Creative - Summarize Video" template
   - Set max_frames to 16-32 based on video length
   - Set max_size to 256-512 based on GPU memory

3. **Processing**:
   - Connect video input to the inference node
   - Execute workflow to get video content summary

#### Object Detection Workflow
1. **Model Setup**:
   - Load Qwen3-VL or GLM-4.6V model
   - Enable mmproj with appropriate visual encoder

2. **Inference Configuration**:
   - Select "Vision - Bounding Box" template
   - Set max_tokens to 1024-2048

3. **Processing**:
   - Connect image input to the inference node
   - Use `JSON to Bounding Box` node to visualize results

### 3. Best Practices

#### Model Selection
- **For high-end GPUs (16GB+ VRAM)**: Use Qwen3-VL, GLM-4.6V, or MiniCPM-V-4_5
- **For mid-range GPUs (8-12GB VRAM)**: Use LLaVA-1.6, Moondream2
- **For low-end GPUs (4-6GB VRAM)**: Use MobileVLM, TinyLLaVA
- **For CPU-only systems**: Use nanoLLaVA, MiniGPT-v2

#### Performance Optimization
- **GPU Usage**: Maximize GPU layers (`n_gpu_layers=-1`) for best performance
- **Memory Management**: Use smaller context length for limited VRAM
- **Batch Processing**: Process multiple images sequentially to optimize memory usage
- **Resource Release**: Always clean sessions and unload models when done

#### Quality Improvement
- **Prompt Engineering**: Use detailed, specific prompts for better results
- **Parameter Tuning**: Adjust temperature, top_p, and top_k based on task type
- **Template Selection**: Choose appropriate prompt templates for specific tasks
- **Model Chaining**: Combine results from different models for complex tasks

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

## Frequently Asked Questions (FAQ)

### 1. Model Loading Issues

**Q: Why is my model not loading?**
- **A:** Check the following:
  - Ensure the model file exists in the correct path (`ComfyUI/models/LLM`)
  - Verify that you're using a compatible GGUF or Safetensors format
  - For VLM models, make sure you have the corresponding mmproj file
  - Update llama-cpp-python to the latest version

**Q: The plugin can't find my model files.**
- **A:** Make sure you've created the `LLM` folder in `ComfyUI/models/` and placed your model files there.

### 2. Performance Issues

**Q: How can I improve inference speed?**
- **A:**
  - Use GPU mode with maximum `n_gpu_layers` (-1)
  - Reduce `n_ctx` to a smaller value
  - Use a smaller, more efficient model
  - Close other GPU-intensive applications

**Q: I'm getting "Out of Memory" (OOM) errors.**
- **A:**
  - Reduce `n_gpu_layers` value
  - Decrease `n_ctx` length
  - Use a smaller model
  - Try CPU mode if GPU memory is insufficient
  - Lower image `max_size` for VLM tasks

### 3. Quality Issues

**Q: The generated text quality is poor.**
- **A:**
  - Use a higher quality model
  - Improve your prompt with more details
  - Adjust temperature, top_p, and other sampling parameters
  - Use appropriate prompt templates for your task

**Q: The model isn't understanding images correctly.**
- **A:**
  - Ensure you're using a VLM model with mmproj enabled
  - Check that the mmproj file matches your model
  - Try increasing `max_size` for better image resolution
  - Use a more capable VLM model like Qwen3-VL or LLaVA-1.6

### 4. General Questions

**Q: Can I use this plugin with any GGUF model?**
- **A:** The plugin supports most GGUF models, but VLM functionality requires specific vision-enabled models and corresponding mmproj files.

**Q: How do I know if I'm using GPU or CPU mode?**
- **A:** Check the console output for device mode information:
  - GPU mode: `[Device Mode] Using GPU mode (n_gpu_layers=X, vram_limit=XGB)`
  - CPU mode: `[Device Mode] Using CPU mode (ignoring n_gpu_layers and vram_limit parameters)`

**Q: Can I run multiple models simultaneously?**
- **A:** Yes, but be aware of memory constraints. It's recommended to unload one model before loading another to avoid OOM errors.

**Q: How often should I update the plugin?**
- **A:** Regularly check for updates to get the latest features, bug fixes, and model support. Use `git pull` in the plugin directory to update.

## Credits  
- [llama-cpp-python](https://github.com/JamePeng/llama-cpp-python) @JamePeng  
- [ComfyUI-llama-cpp](https://github.com/kijai/ComfyUI-llama-cpp) @kijai  
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) @comfyanonymous
