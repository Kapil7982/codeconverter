from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

GPT_API_KEY = 'paste_your_api_key_here'

def handle_code_conversion(code, target_language):
    prompt = f'Convert the following {target_language} code to {target_language}:\n\n{code}'
    response = requests.post('https://api.openai.com/v1/chat/completions', json={
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': prompt
            }
        ]
    }, headers={
        'Authorization': f'Bearer {GPT_API_KEY}'
    })

    return response.json()['choices'][0]['message']

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.get_json()
    code = data['code']
    target_language = data['targetLanguage']
    try:
        converted_code = handle_code_conversion(code, target_language)
        return jsonify({'output': converted_code})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Something went wrong'}), 500

# Debugging and quality check endpoints

def handle_code_debugging(code, target_language):
    prompt = f'Debug the following {target_language} code:\n\n{code}'
    response = requests.post('https://api.openai.com/v1/chat/completions', json={
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': prompt
            }
        ]
    }, headers={
        'Authorization': f'Bearer {GPT_API_KEY}'
    })

    return response.json()['choices'][0]['message']

@app.route('/api/debug', methods=['POST'])
def debug():
    data = request.get_json()
    code = data['code']
    target_language = data['targetLanguage']
    try:
        debugging_output = handle_code_debugging(code, target_language)
        return jsonify({'debuggingOutput': debugging_output})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Something went wrong'}), 500

def handle_code_quality_check(code, target_language):
    prompt = f'Check the quality of the following {target_language} code:\n\n{code}'
    response = requests.post('https://api.openai.com/v1/chat/completions', json={
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': prompt
            }
        ]
    }, headers={
        'Authorization': f'Bearer {GPT_API_KEY}'
    })

    return response.json()['choices'][0]['message']

@app.route('/api/quality', methods=['POST'])
def quality():
    data = request.get_json()
    code = data['code']
    target_language = data['targetLanguage']
    try:
        quality_output = handle_code_quality_check(code, target_language)
        return jsonify({'qualityOutput': quality_output})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    app.run(port=5000)
