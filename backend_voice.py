from bottle import route, run, request, response, static_file
from llama_cpp import Llama
import time
import os
from text_to_speech import text_to_speech

# Enable MacBook M2 metal with n_gpu_layers=-1
llm = Llama(
    model_path="mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_gpu_layers=-1,
    n_ctx=4096  # Increased context window
)

@route('/')
def index():
    return static_file('index_voice.html', root='.')

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
    
    response_text = output['choices'][0]['text'].strip()
    
    # Generate unique filename for this response
    filename = f"response_{int(time.time())}.wav"
    
    # Convert response to speech
    audio_path = text_to_speech(response_text, output_path=filename)
    
    if audio_path:
        response.content_type = 'application/json'
        return {
            'response': response_text,
            'audio_file': filename
        }
    else:
        response.content_type = 'application/json'
        return {
            'response': response_text,
            'audio_file': None
        }

@route('/audio/<filename>')
def serve_audio(filename):
    return static_file(filename, root='.', mimetype='audio/wav')

run(host='localhost', port=8080)