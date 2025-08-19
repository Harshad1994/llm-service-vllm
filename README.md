# LLM Service with vLLM

A FastAPI service leveraging vLLM's paged attention for high-performance LLM inference.

## Features

- Support for multiple LLM models (Llama-2, Llama-3)
- Efficient inference using paged attention
- Quantization support (AWQ, GPT-Q)
- Multi-GPU parallel processing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/llm-service-vllm.git
cd llm-service-vllm
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Llama-2-13b
```bash
python main.py \
    --model meta-llama/Llama-2-13b-hf \
    --tensor-parallel-size 4 \
    --download-dir /datadisk/harshad/download_dir \
    --gpu-memory-utilization 0.6
```

### Running Llama-2-70b with AWQ Quantization
```bash
python main.py \
    --model TheBloke/Llama-2-70B-chat-AWQ \
    --tensor-parallel-size 4 \
    --download-dir /datadisk/llms/model_dir \
    --gpu-memory-utilization 0.6 \
    --quantization awq
```

### Running Llama-3-8b
```bash
python main.py \
    --model meta-llama/Llama-3-8b-hf \
    --tensor-parallel-size 4 \
    --download-dir /datadisk/harshad/download_dir \
    --gpu-memory-utilization 0.6
```

## Configuration

| Argument | Description |
|----------|-------------|
| `--model` | HuggingFace model identifier |
| `--tensor-parallel-size` | Number of GPUs to utilize |
| `--download-dir` | Model storage directory |
| `--gpu-memory-utilization` | GPU memory usage (0.0-1.0) |
| `--quantization` | Quantization method (AWQ, GPT-Q) |

## Contributing

Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

Apache 2.0 - Pls see LICENSE file for more details
