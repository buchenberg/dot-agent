---
name: mlops/vllm-ubuntu-setup
description: >
  Complete guide to installing and configuring vLLM on Ubuntu for high-throughput
  LLM inference. Covers GPU setup, Python environment creation, vLLM installation,
  model downloading, OpenAI-compatible API server configuration, quantized model
  deployment, systemd service setup, benchmarking, and troubleshooting. Based on
  the OneUptime guide (2026-03-02).
triggers:
  - vLLM installation on Ubuntu
  - LLM inference server setup
  - OpenAI-compatible API server self-hosting
  - vLLM configuration and optimization
  - Quantized model deployment (AWQ, GPTQ, bitsandbytes)
  - vLLM troubleshooting (OOM, slow downloads, CUDA errors)
  - PagedAttention and KV cache optimization
---

# vLLM Ubuntu Setup Skill

## Overview

vLLM is a high-performance library for LLM (Large Language Model) inference. It implements **PagedAttention** — an efficient memory management algorithm for the KV cache — which significantly increases throughput compared to naive implementations. It also provides an **OpenAI-compatible REST API server**, making it easy to swap in as a backend for applications that already use the OpenAI API.

**Key benefits:**
- Up to 24x higher throughput than Hugging Face Transformers (original vLLM benchmarks)
- Efficient batching of requests with different sequence lengths
- Continuous batching (new requests added to existing batches)
- OpenAI-compatible API — drop-in replacement for OpenAI endpoints

---

## Prerequisites

| Requirement | Specification |
|-------------|---------------|
| OS | Ubuntu 22.04 or 24.04 |
| GPU | NVIDIA GPU with at least 16GB VRAM (24GB+ recommended for 7B models) |
| Driver | NVIDIA driver new enough for the CUDA backend selected by PyTorch/vLLM |
| Python | 3.10–3.13 |
| RAM | At least 32GB system RAM |

> **Note:** For smaller GPUs, quantized models (GPTQ, AWQ, bitsandbytes) reduce VRAM requirements significantly.

---

## Step 1: Verify GPU Setup

```bash
# Check GPU and driver
nvidia-smi

# Check CUDA version
nvcc --version || nvidia-smi | grep "CUDA Version"

# Check available GPU memory
nvidia-smi --query-gpu=memory.total,memory.free --format=csv
```

---

## Step 2: Create Python Environment

```bash
# Install Python, venv, curl, and uv
sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv curl
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"

# Create a dedicated venv
uv venv --python 3.12 --seed --managed-python ~/vllm-env
source ~/vllm-env/bin/activate

# Upgrade pip
pip install --upgrade pip
```

---

## Step 3: Install vLLM

```bash
# Install vLLM with a PyTorch backend selected for your CUDA driver
uv pip install vllm --torch-backend=auto

# This installs PyTorch with CUDA, vLLM, and all dependencies
# Installation can take 10-20 minutes due to large CUDA packages

# Verify installation
python3 -c "import vllm; print(vllm.__version__)"
```

---

## Step 4: Download a Model

vLLM loads models from Hugging Face Hub. Some models require accepting usage agreements on the HF website.

```bash
# Install huggingface_hub for model downloading
pip install huggingface_hub

# Optional: authenticate for gated models
huggingface-cli login

# Pre-download a model (optional - vLLM downloads on first use)
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='meta-llama/Llama-3.2-1B-Instruct',  # Small model for testing
    # repo_id='meta-llama/Meta-Llama-3-8B-Instruct',  # 8B model, needs 16GB VRAM
    local_dir='/opt/models/llama-3.2-1b-instruct'
)
"
```

---

## Step 5: Run vLLM as an OpenAI-Compatible Server

### Basic Server Start

```bash
# Start the server with a small model
vllm serve meta-llama/Llama-3.2-1B-Instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --served-model-name "llama-3.2-1b"

# Or use a locally downloaded model
vllm serve /opt/models/llama-3.2-1b-instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --served-model-name "llama-3.2-1b"
```

### Production Server Options

```bash
vllm serve meta-llama/Meta-Llama-3-8B-Instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 2 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.90 \
  --dtype bfloat16 \
  --max-num-seqs 256 \
  --enable-chunked-prefill \
  --api-key "your-secret-key"
```

| Flag | Description |
|------|-------------|
| `--tensor-parallel-size 2` | Uses 2 GPUs |
| `--max-model-len 4096` | Limits context length to reduce VRAM usage |
| `--gpu-memory-utilization 0.90` | Reserves 90% of GPU memory for vLLM |
| `--dtype bfloat16` | Suitable for GPUs with BF16 support |
| `--max-num-seqs 256` | Controls concurrent sequences |
| `--enable-chunked-prefill` | Improves scheduling for long prompts |
| `--api-key "key"` | Requires API key for authentication |

---

## Querying the Server

### cURL Examples

```bash
# Chat completion
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b",
    "messages": [
      {"role": "user", "content": "Explain what a KV cache is in 2 sentences."}
    ],
    "max_tokens": 200,
    "temperature": 0.7
  }'

# Text completion
curl http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2-1b",
    "prompt": "The capital of France is",
    "max_tokens": 50
  }'

# List available models
curl http://localhost:8000/v1/models
```

### Python Client

```python
#!/usr/bin/env python3
# pip install openai

from openai import OpenAI

# Point the client to your local vLLM server
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"  # Can be any string if no auth configured
)

# Simple completion
response = client.chat.completions.create(
    model="llama-3.2-1b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the difference between a process and a thread?"}
    ],
    max_tokens=300,
    temperature=0.7,
    stream=False
)
print(response.choices[0].message.content)

# Streaming response
stream = client.chat.completions.create(
    model="llama-3.2-1b",
    messages=[{"role": "user", "content": "Write a short poem about Linux."}],
    max_tokens=200,
    stream=True
)
print("Streaming response:", end="", flush=True)
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()
```

---

## Using Quantized Models

For GPUs with less VRAM, quantized models reduce memory requirements:

```bash
# AWQ quantized model (very fast inference)
vllm serve TheBloke/Llama-2-7B-AWQ \
  --quantization awq \
  --max-model-len 4096

# GPTQ quantized model
vllm serve TheBloke/Llama-2-13B-chat-GPTQ \
  --quantization gptq

# BitsAndBytes (4-bit)
vllm serve meta-llama/Meta-Llama-3-8B-Instruct \
  --quantization bitsandbytes \
  --load-format bitsandbytes \
  --tensor-parallel-size 4
```

---

## Running as a Systemd Service

```bash
sudo tee /etc/systemd/system/vllm.service << 'EOF'
[Unit]
Description=OpenAI-Compatible Server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
Environment="PATH=/home/ubuntu/vllm-env/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Environment="HOME=/opt/models"
Environment="HF_HOME=/opt/models"
ExecStart=/home/ubuntu/vllm-env/bin/vllm serve meta-llama/Llama-3.2-1B-Instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --served-model-name llama-3.2-1b \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.90
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable vllm
sudo systemctl start vllm
sudo journalctl -u vllm -f
```

---

## Benchmarking Throughput

vLLM includes built-in benchmarking tools:

```bash
# Install benchmarking dependencies
pip install aiohttp

# Run offline throughput benchmark
vllm bench throughput \
  --backend vllm \
  --model meta-llama/Llama-3.2-1B-Instruct \
  --dataset-name sharegpt \
  --dataset-path /path/to/ShareGPT_V3_unfiltered_cleaned_split.json \
  --num-prompts 1000

# Online serving benchmark (requires server to be running!)
vllm bench serve \
  --model llama-3.2-1b \
  --base-url http://localhost:8000 \
  --num-prompts 100 \
  --request-rate 10  # requests per second
```

---

## Troubleshooting

### CUDA Out of Memory During Model Loading

```bash
# Reduce max model length
--max-model-len 2048  # Reduces KV cache size

# Use quantization to reduce model weights size
--quantization awq

# Reduce GPU memory utilization
--gpu-memory-utilization 0.80
```

### Model Downloads Extremely Slowly

```bash
# Enable fast downloads
HF_HUB_ENABLE_HF_TRANSFER=1 pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

### Server Starts But Returns Errors

```bash
# Check if the model name matches in the request
curl http://localhost:8000/v1/models

# View server logs for detailed errors
sudo journalctl -u vllm --since "5 minutes ago" -f
```

### Slow First Request

- vLLM warms up the CUDA kernels on the first request — this is normal
- Subsequent requests are much faster
- Consider sending a warmup request after startup

---

## Key Takeaways

1. **OpenAI compatibility** means you can serve models locally and swap the endpoint in existing applications by just changing the base URL — no code changes required.
2. **PagedAttention** manages KV cache like virtual memory pages, enabling efficient memory use and cache sharing.
3. **Quantization** (AWQ, GPTQ, bitsandbytes) makes it possible to run larger models on GPUs with limited VRAM.
4. **Systemd service** setup ensures vLLM starts automatically and restarts on failure.
5. **Benchmarking tools** (`vllm bench throughput`, `vllm bench serve`) help validate performance before production deployment.
