import os
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

from ai import generate_command, is_safe
from utils import execute_command

load_dotenv()  

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_ui():
    return send_from_directory('static', 'index.html')

@app.route('/api/command', methods=['POST'])
def run_command():
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()
    if not prompt:
        return jsonify({'error': 'Please provide a prompt.'}), 400

    cmd = generate_command(prompt)
    if not is_safe(cmd):
        return jsonify({'command': cmd, 'output': '🚨 Blocked as unsafe'}), 403

    output = execute_command(cmd)
    return jsonify({'command': cmd, 'output': output})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
