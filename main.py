from bottle import route, run, request, response, static_file
from llama_cpp import Llama
import time

# Enable MacBook M2 metal with n_gpu_layers=-1
llm = Llama(
    model_path="mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_gpu_layers=-1,
    n_ctx=4096  # Increased context window
)

@route('/')
def index():
    return static_file('index.html', root='.')

@route('/chat', method='POST')
def chat():
    message = request.json.get('message', '')
    
    # Format prompt for Mistral instruct model
    prompt = f"""<s>[INST] Please provide a brief response that keeps the conversation going in 1-3 sentences: {message} [/INST]"""
    
    # Generate response
    output = llm(
        prompt,
        max_tokens=256,  # Reduced for shorter responses
        temperature=0.7,
        stop=["</s>", "[INST]"],  # Stop at end of response or new instruction
        echo=False  # Don't include prompt in output
    )
    
    response.content_type = 'application/json'
    return {'response': output['choices'][0]['text'].strip()}

run(host='localhost', port=8080)