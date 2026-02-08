# **llama-cpp-python 0.3.23 Compatible Models Download and Preset Recommendations**



### Note: Please download based on your needs and hardware environment. Different models are suitable for different scenarios such as ComfyUI prompt generation, image/video frame reverse inference, etc. Reverse inference requires matching mmproj visual models.



### Quantization Level Selection

- **Q4_K_M**: Balanced size and quality (recommended)
- **Q5_K_M**: Higher quality, slightly larger file
- **Q3_K_M**: Smaller file, suitable for low VRAM devices
- **Q2_K**: Smallest file, lower quality


### Model Preparation

1. **Create model directory**:

   - Create an `LLM` folder under `ComfyUI/models/` directory
   - Place downloaded model files in this directory. If you download multiple models, it's recommended to create subfolders within the LLM folder for easier differentiation


2. **Model file format**:

   - Supports `.gguf` and `.safetensors` formats
   - Visual models require corresponding `mmproj` files




### Qwen-VL Series

**Model Series**: Qwen-VL
**Specific Model**: Qwen2.5-VL
**Core Features**: Alibaba Tongyi Qianwen multimodal series, full-size coverage, balanced multilingual OCR and image-text reasoning.
**Applicable Scenarios**: Multilingual OCR, image/video frame reverse inference, prompt generation, general image-text Q&A, batch text extraction
**Download Link (nsfw)**: https://huggingface.co/mradermacher/Qwen2.5-VL-7B-Instruct-abliterated-GGUF (includes mmproj model)



**Model Series**: Qwen-VL
**Specific Model**: Qwen3-VL-Instruct
**Core Features**: Qwen3-VL instruction-optimized version, highest instruction following accuracy, supports complex visual instruction execution (e.g., "extract all tables from images and generate text").
**Applicable Scenarios**: Instruction-based OCR extraction, complex image-text reverse inference, professional visual task processing, high-precision prompt generation
**Download Link (nsfw)**: https://huggingface.co/mradermacher/Qwen3-VL-8B-Instruct-abliterated-v2.0-GGUF (includes mmproj model)



### OCR Specialized Series

**Model Series**: olmOCR
**Specific Model**: olmOCR-2-7B-1025

**Core Features**: OCR-specialized fine-tuned, supports formula, table, and old scanned document recognition, high text extraction accuracy, no additional modifications needed, excellent local inference efficiency.
**Applicable Scenarios**: Poster text recognition, document OCR, text extraction, academic paper formula recognition, batch scanned document text extraction
**Download Link**: https://huggingface.co/Mungert/olmOCR-2-7B-1025-GGUF (includes mmproj model)



### LLaMA Series

**Model Series**: LLaVA
**Specific Model**: llava-1.6-mistral-7b
**Core Features**: General multimodal benchmark model, stable image-text alignment, balanced visual reasoning capabilities.
**Applicable Scenarios**: Image reverse prompt generation, simple OCR text extraction, general image-text Q&A, video frame key information recognition
**Download Link**: https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf (includes mmproj model)



**Model Series**: nanoLLaVA
**Specific Model**: nanoLLaVA-1.5
**Core Features**: LLaVA lightweight compact version, small parameter count, low VRAM usage, fast inference speed, extremely low local deployment threshold, strong adaptability for basic visual tasks.
**Applicable Scenarios**: Low-end device image reverse inference, simple text extraction, batch fast image annotation, edge device local deployment
**Download Link**: https://huggingface.co/qnguyen3/nanoLLaVA-1.5

**mmproj model**: https://huggingface.co/saiphyohein/nanollava-1.5-gguf



### MiniCPM-V Series

**Model Series**: MiniCPM-V
**Specific Model**: MiniCPM-V-4.5
**Core Features**: Domestic lightweight multimodal flagship, balances accuracy and speed, supports arbitrary aspect ratio image recognition, excellent OCR capabilities, complete ComfyUI node adaptation.
**Applicable Scenarios**: Prompt generation, image/video frame reverse inference, multilingual OCR, batch image text extraction, daily visual reasoning
**Download Link**: https://huggingface.co/openbmb/MiniCPM-V-4_5-gguf (includes mmproj model)



**Model Series**: MiniCPM-V
**Specific Model**: MiniCPM-Llama3-V 2.5
**Core Features**: Optimized based on Llama3 base, lightweight and efficient, improved image-text fusion capabilities, high batch inference efficiency, strong local deployment stability.
**Applicable Scenarios**: Batch image reverse inference, fast prompt generation, lightweight OCR, low-config device ComfyUI workflows
**Download Link**: https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5-gguf (includes mmproj model)



### GLM Series

**Model Series**: GLM-4 Visual Edition
**Specific Model**: GLM-4.6V
**Core Features**: Zhipu large-parameter multimodal model, top-tier OCR and complex document parsing capabilities, supports high-resolution image recognition, stable local inference, adapts to complex visual tasks.
**Applicable Scenarios**: Professional OCR text extraction, complex document/table recognition, academic paper parsing, high-precision image reverse inference, multilingual image-text reasoning
**Download Link (nsfw)**: https://huggingface.co/huihui-ai/Huihui-GLM-4.6V-Flash-abliterated-GGUF (includes mmproj model)



### JoyCaption Series

**Model Series**: JoyCaption
**Specific Model**: llama-joycaption
**Core Features**: ComfyUI-specific prompt generation/image reverse inference model, strong detail capture ability, generated prompts fit creative needs.
**Applicable Scenarios**: ComfyUI prompt generation, precise image reverse inference, artistic creation image-text association, batch image tag generation
**Download Link (nsfw)**: https://huggingface.co/mradermacher/llama-joycaption-beta-one-hf-llava-GGUF

**mmproj model**: https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf



### Moondream Series

**Model Series**: Moondream
**Specific Model**: Moondream2
**Core Features**: Ultra-lightweight multimodal model (only 1.4B parameters), extremely fast inference, very low VRAM usage (runs on 4GB VRAM), sufficient for basic visual and OCR tasks.
**Applicable Scenarios**: Edge device local deployment, batch fast image reverse inference, simple text extraction, low-end computer ComfyUI workflows
**Download Link**: https://huggingface.co/Hahasb/moondream2-20250414-GGUF (includes mmproj model)



### Gemma Series

**Model Series**: Gemma
**Specific Model**: gemma-3-12b
**Core Features**: Google Gemma 3 series multimodal model, featuring visual-language understanding, long context processing capabilities, and enhanced multilingual support, runs on a single GPU, outperforming models with the same parameter count.
**Applicable Scenarios**: Multilingual prompt generation, complex visual reasoning, long text understanding, multimodal interaction tasks
**Download Link**: https://huggingface.co/unsloth/gemma-3-12b-it-GGUF (includes mmproj model)



### Youtu-VL Series

**Model Series**: Youtu-VL
**Specific Model**: Youtu-VL-4B-Instruct
**Core Features**: Tencent YouTu Lab multimodal visual-language model, 4B parameter lightweight design, excellent performance in visual understanding and language generation, supports bilingual (Chinese-English) processing.
**Applicable Scenarios**: Image understanding and description, visual question answering, OCR text extraction, bilingual prompt generation
**Download Link**: https://huggingface.co/tencent/Youtu-VL-4B-Instruct-GGUF (includes mmproj model)



### EraX-VL Series

**Model Series**: EraX-VL
**Specific Model**: EraX-VL-7B-V1.5
**Core Features**: 7B parameter multimodal visual-language model, V1.5 version further enhances visual perception and language understanding capabilities, supports high-resolution image processing, strong instruction following ability.
**Applicable Scenarios**: Image reverse inference, visual question answering, complex scene understanding, instruction-based prompt generation
**Download Link**: https://huggingface.co/mradermacher/EraX-VL-7B-V1.5-GGUF (includes mmproj model)



### MiMo-VL Series

**Model Series**: MiMo-VL
**Specific Model**: MiMo-VL-7B-RL
**Core Features**: Xiaomi open-source multimodal visual-language model, 7B parameters, trained based on reinforcement learning, four-stage pre-training (projector warm-up, visual-language alignment, general multimodal pre-training, long context supervised fine-tuning), outperforms 100B+ models with small parameter count.
**Applicable Scenarios**: Chinese-English bilingual dialogue, complex visual reasoning, multimodal interaction, long context understanding, creative prompt generation
**Download Link**: https://huggingface.co/unsloth/MiMo-VL-7B-RL-GGUF (includes mmproj model)



### DreamOmni Series

**Model Series**: DreamOmni
**Specific Model**: DreamOmni2
**Core Features**: Cross-modal multimodal model, supports image-text combined reasoning, prompt generation fits creative needs, adapts to ComfyUI creative workflows.
**Applicable Scenarios**: Creative prompt generation, image reverse inference, audio-image-text fusion creation (audio functionality requires additional components), complex visual scene reasoning
**Download Link**: https://huggingface.co/rafacost/DreamOmni2-7.6B-GGUF (includes mmproj model)




### Phi Vision Series

**Model Series**: Phi-Vision
**Specific Model**: Phi-3.5-vision-instruct
**Core Features**: Microsoft iterative multimodal model, optimized for multi-image/video frame sequence reverse inference, high instruction following accuracy, adapts to ComfyUI video frame processing nodes.
**Applicable Scenarios**: Video frame reverse inference, multi-image comparison reverse inference, instruction-based prompt generation, general OCR text extraction
**Download Link**: https://huggingface.co/abetlen/Phi-3.5-vision-instruct-gguf (includes mmproj model)





### LLaMA Vision Series

**Model Series**: LLaMA-Vision
**Specific Model**: Llama-3.2-11B-Vision-Instruct
**Core Features**: Meta official multimodal model, balanced across all scenarios, strong complex visual reasoning capabilities, supports high-resolution image recognition, adapts to various ComfyUI visual tasks.
**Applicable Scenarios**: High-precision image reverse inference, complex document OCR, video frame key information extraction, professional-level visual reasoning
**Download Link**: https://huggingface.co/leafspark/Llama-3.2-11B-Vision-Instruct-GGUF (includes mmproj model)



**Model Series**: LLaMA-Vision
**Specific Model**: LLaMA-3.1-Vision
**Core Features**: Predecessor of Llama-3.2-Vision, stable image-text understanding capabilities, suitable for use as a basic visual model.
**Applicable Scenarios**: General image reverse inference, basic OCR text extraction, simple visual reasoning, backup basic visual model
**Download Link**: https://huggingface.co/FiditeNemini/Llama-3.1-Unhinged-Vision-8B-GGUF (includes mmproj model)



### Yi-VL Series

**Model Series**: Yi-VL
**Specific Model**: Yi-VL-6B
**Core Features**: Domestic long-context multimodal model, balanced Chinese-English OCR capabilities, high image-text understanding accuracy, supports long image-text joint reasoning, adapts to bilingual document scenarios.
**Applicable Scenarios**: Bilingual document OCR, long image-text reverse inference, Chinese-English bilingual prompt generation, bilingual visual reasoning tasks
**Download Link**: https://huggingface.co/cmp-nct/Yi-VL-6B-GGUF (includes mmproj model)



### LightOnOCR Series

**Model Series**: LightOnOCR
**Specific Model**: LightOnOCR-2-1B
**Core Features**: Ultra-lightweight OCR-specific model, only 1B parameters, extremely fast inference speed, very low VRAM usage (runs on 2GB VRAM), focused on text extraction tasks, suitable for batch processing.
**Applicable Scenarios**: Batch text extraction, simple OCR tasks, low VRAM devices, fast document scanning, edge device deployment
**Download Link**: https://huggingface.co/noctrex/LightOnOCR-2-1B-GGUF (includes mmproj model)



## Preset Template Recommended Models

### Basic Templates

**Empty Template**: Empty template, fully customizable

**Applicable Models**: None (select all models as needed)



**Simple Description**: Simply describe image content

**Recommended Models**: Qwen3-VL-Instruct、LLaVA-1.6、nanoLLaVA、Moondream2、LLaMA-3.1-Vision、llama-joycaption、LightOnOCR-2-1B



### Prompt Style Templates

**Tag Style**: Generate image tag lists, suitable for models like SDXL, outputs up to 60 unique tags

**Recommended Models**: Qwen3-VL-Instruct、DreamOmni2、MiniCPM-V-4.5、llama-joycaption



**Concise Description**: Concise image description (within 300 words), enhances clarity and expressiveness

**Recommended Models**: Qwen3-VL-Instruct、nanoLLaVA、Moondream2、LLaMA-3.1-Vision、Qwen2.5-VL、llama-joycaption、GLM-4.6V、Youtu-VL-4B-Instruct



**Detailed Description**: Detailed image description (within 500 words), adds specific details for each element

**Recommended Models**: Qwen3-VL-Instruct、LLaVA-1.6、MiniCPM-V-4.5、DreamOmni2、GLM-4.6V、EraX-VL-7B-V1.5



**Detailed Expansion**: Detailed prompt expansion (within 800 words), enhances clarity and expressiveness

**Recommended Models**: Qwen3-VL-Instruct、DreamOmni2、Llama-3.2-11B-Vision-Instruct、GLM-4.6V、gemma-3-12b



**Optimized Expansion**: Optimize and expand prompts to make them more expressive and visually rich

**Recommended Models**: Qwen3-VL-Instruct、DreamOmni2、GLM-4.6V、MiMo-VL-7B-RL



### Creative Templates

**Detailed Analysis**: Detailed analysis of image content, breaking down subject, clothing, accessories, background and composition

**Recommended Models**: Llama-3.2-11B-Vision-Instruct、Qwen3-VL-Instruct、GLM-4.6V、EraX-VL-7B-V1.5



**Video Summary**: Summarize key events and narrative points of video content

**Recommended Models**: Qwen3-VL-Instruct、Phi-3.5-vision-instruct、GLM-4.6V、MiMo-VL-7B-RL



**Short Story**: Generate short stories based on images or videos

**Recommended Models**: Qwen3-VL-Instruct、DreamOmni2、GLM-4.6V、gemma-3-12b



### Visual Templates

**Bounding Box Detection**: Generate object detection bounding boxes, output JSON format coordinate lists

**Recommended Models**: LLaVA-1.6、Llama-3.2-11B-Vision-Instruct、Qwen3-VL-Instruct




### OCR Templates

**OCR Enhanced**: Professional poster OCR text recognition, accurately extracts text content and style attributes, adapts to prompt reverse inference needs

**Recommended Models**: olmOCR-2、GLM-4.6V、Qwen3-VL-Instruct、LightOnOCR-2-1B



### Multilingual Templates

**Chinese-English Bilingual Generation**: Chinese-English bilingual prompt generation, adapts to cross-border creation / bilingual document scenarios

**Recommended Models**: Qwen2.5-VL、GLM-4.6V



### High Resolution Templates

**Ultra HD Reverse Inference**: Ultra HD image prompt reverse inference, supports 4K/8K resolution image detail extraction

**Recommended Models**: Llama-3.2-11B-Vision-Instruct、GLM-4.6V




### Video Templates

**Video Reverse Inference**: Video reverse inference prompts, generate detailed video descriptions based on video content

**Recommended Models**: Qwen3-VL-Instruct、Phi-3.5-vision-instruct、GLM-4.6V、MiMo-VL-7B-RL



**Video Scene Deconstruction**: Detailed video scene deconstruction, provides complete details for each scene in chronological order

**Recommended Models**: Qwen3-VL-Instruct、Phi-3.5-vision-instruct、Llama-3.2-11B-Vision-Instruct、GLM-4.6V、MiMo-VL-7B-RL



**Video Subtitle Format**: Generate standard format video subtitles, including timecodes and synchronized text

**Recommended Models**: Phi-3.5-vision-instruct、Qwen2.5-VL、Youtu-VL-4B-Instruct



### Professional Model Templates

**ZIMAGE-Turbo**: Designed specifically for Z-Image-Turbo model, creates efficient and high-quality image generation prompts, uses 8-step Turbo inference to quickly generate 1080P HD images

**Recommended Models**: Qwen3-VL-Instruct、DreamOmni2、GLM-4.6V、Youtu-VL-4B-Instruct



**FLUX2-Klein**: Designed specifically for FLUX.2 Klein model, creates concise and expressive prompts (within 200 words)

**Recommended Models**: Qwen3-VL-Instruct、nanoLLaVA、Moondream2、MiniCPM-Llama3-V 2.5、Qwen2.5-VL、GLM-4.6V、Youtu-VL-4B-Instruct



**LTX-2**: Designed specifically for LTX-2 model, creates detailed and dynamic video generation prompts, supports high-quality, audio-visual synchronized 4K video

**Recommended Models**: Phi-3.5-vision-instruct、Llama-3.2-11B-Vision-Instruct、GLM-4.6V、EraX-VL-7B-V1.5



**Qwen Layered Image**: Designed specifically for Qwen-Image-Layered model, creates detailed layered prompts, handles complex compositions and multiple elements

**Recommended Models**: Qwen2.5-VL、Qwen3-VL-Instruct、GLM-4.6V、EraX-VL-7B-V1.5



**Qwen Image Edit**: Comprehensive edit prompt enhancer, used for image editing tasks, supports adding, deleting, replacing operations

**Recommended Models**: Qwen3-VL-Instruct、DreamOmni2、GLM-4.6V、MiMo-VL-7B-RL



**Qwen2512**: Designed specifically for Qwen Image2512 model, creates high-quality image generation prompts

**Recommended Models**: Qwen2.5-VL、Qwen3-VL-Instruct、LLaVA-1.6、GLM-4.6V、Youtu-VL-4B-Instruct



### Film Style Templates

**WAN Text to Video**: Film director style, adds film elements to original prompt (time, light source, light intensity, light angle, tone, shooting angle, shot size, composition, etc.)

**Recommended Models**: DreamOmni2、Llama-3.2-11B-Vision-Instruct、Qwen3-VL-Instruct、GLM-4.6V、MiMo-VL-7B-RL



**WAN Image to Video**: Video description prompt rewriting expert, rewrites video descriptions based on images and input prompts, emphasizes dynamic content

**Recommended Models**: Phi-3.5-vision-instruct、Qwen3-VL-Instruct、GLM-4.6V、EraX-VL-7B-V1.5



**WAN Image to Video Empty Template**: Video description prompt writing expert, generates video descriptions based on images using imagination

**Recommended Models**: DreamOmni2、llama-joycaption、GLM-4.6V



**WAN First/Last Frame to Video**: Prompt optimizer, optimizes and rewrites prompts based on video first/last frame images, emphasizes motion information and camera movement

**Recommended Models**: Phi-3.5-vision-instruct、Llama-3.2-11B-Vision-Instruct、GLM-4.6V、EraX-VL-7B-V1.5
