import os
import requests
from dotenv import load_dotenv
from prompts import get_command_prompt, get_safety_prompt

load_dotenv()

BASE_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
MODEL = os.getenv("LLAMA_MODEL", "llama3")

def generate_command(user_input):
    response = requests.post(
        f"{BASE_URL}/api/chat",
        json={
            "model": MODEL,
            "stream": False,  # ← prevent streaming!
            "messages": [
                {"role": "system", "content": get_command_prompt()},
                {"role": "user", "content": user_input}
            ]
        }
    )
    response.raise_for_status()
    return response.json()['message']['content'].strip()

def is_safe(command):
    response = requests.post(
        f"{BASE_URL}/api/chat",
        json={
            "model": MODEL,
            "stream": False,  # ← prevent streaming here too
            "messages": [
                {"role": "user", "content": get_safety_prompt(command)}
            ]
        }
    )
    response.raise_for_status()
    return "safe" in response.json()['message']['content'].lower()
