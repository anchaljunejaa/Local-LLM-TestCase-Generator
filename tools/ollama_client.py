import requests
import json
import os

def call_ollama(prompt, model="llama3.2"):
    """
    Deterministically calls the local Ollama API.
    """
    url = "http://127.0.0.1:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json" # Force JSON output from the model
    }
    
    try:
        # Increased timeout to 300s to handle slow local generations
        response = requests.post(url, json=payload, timeout=300)

        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to Ollama. {str(e)}"


if __name__ == "__main__":
    # Test call
    test_prompt = "Generate a JSON object with one key 'status' and value 'connected'"
    print(call_ollama(test_prompt))
