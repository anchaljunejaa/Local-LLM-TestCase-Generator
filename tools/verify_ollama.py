"""
Phase 2: Handshake - Verify Ollama connection
"""
import requests
import json
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def verify_ollama():
    """Test connection to Ollama API"""
    try:
        url = "http://127.0.0.1:11434/api/generate"
        payload = {

            "model": "llama3.2",
            "prompt": "Say 'Hello' and nothing else.",
            "stream": False
        }
        
        print(f"Testing connection to {url} with model 'llama3.2'...")
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            print("Received response: Connection Successful.")
            print("[OK] Handshake Verified: Ollama is running and responding.")
            return True
        else:
            print(f"[ERROR] Received status code {response.status_code}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
        print("Make sure Ollama is running: ollama serve")
        return False

if __name__ == "__main__":
    success = verify_ollama()
    exit(0 if success else 1)

