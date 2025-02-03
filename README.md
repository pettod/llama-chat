# Mistral Chat Interface

This is a simple chat interface for the Mistral 7B model.

## Installation

Macbook

```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python --no-cache-dir
```

Linux GPU

```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --no-cache-dir
```

```bash
wget https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q4_K_M.gguf
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

[http://localhost:8080](http://localhost:8080)
