from bottle import route, run, request, response, static_file
from llama_cpp import Llama
import time

llm = Llama(model_path="mistral-7b-v0.1.Q4_K_M.gguf")

@route('/')
def index():
    return static_file('index.html', root='.')

@route('/chat', method='POST')
def chat():
    message = request.json.get('message', '')
    #output = llm(message, max_tokens=2048, temperature=0.7)
    time.sleep(3)  # Add 3 second delay
    response.content_type = 'application/json'
    return {'response': "Hello, how are you?"} #output['choices'][0]['text']}

run(host='localhost', port=8080)