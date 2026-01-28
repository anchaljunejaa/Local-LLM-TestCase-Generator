import json
from tools.ollama_client import call_ollama

def generate_testcases(requirement_text):
    """
    Constructs the prompt and processes the LLM response.
    """
    if not requirement_text.strip():
        return {"error": "Input requirement text is empty."}

    prompt = f"""
    Requirement: {requirement_text}
    Task: Generate 3-5 professional test cases in JSON format.
    JSON Structure:
    {{
        "test_suite": "...",
        "cases": [
            {{
                "id": "TC-1",
                "title": "...",
                "steps": ["..."],
                "expected": "..."
            }}
        ]
    }}
    """

    
    raw_response = call_ollama(prompt)
    
    if raw_response.startswith("Error:"):
        return {"error": raw_response}
        
    try:
        data = json.loads(raw_response)
        return data
    except json.JSONDecodeError:
        return {
            "error": "LLM failed to return valid JSON.",
            "raw_output": raw_response
        }

if __name__ == "__main__":
    # Test call
    sample_req = "A login page with username and password fields."
    print(json.dumps(generate_testcases(sample_req), indent=2))
