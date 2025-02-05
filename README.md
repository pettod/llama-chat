# Mistral Chat Interface

<video src='https://github.com/user-attachments/assets/4f72b543-1967-4c70-a8f7-c63f44657203' width=540/></video>

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

Better model is here: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

```bash
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF mistral-7b-instruct-v0.2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

## Usage

```bash
python backend_chat.py
python bot.py
```

[http://localhost:8080](http://localhost:8080)
