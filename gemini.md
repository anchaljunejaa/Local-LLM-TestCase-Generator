# Project Constitution (gemini.md)

## Data Schemas

### Core Entities

#### 1. Interaction
- **Input**: `UserScenario` (String) - The description or code snippet provided by the user.
- **Output**: `TestCaseSuite` (Markdown/Code) - The generated test cases.
- **Model**: `llama3.2` (Default).

### API Interface (Internal)

#### Request Object
```json
{
  "input_data": "User's raw input string",
  "system_prompt": "The defined template stored in code",
  "model": "llama3.2"
}
```

#### Response Object
```json
{
  "test_cases": "Generated text content",
  "metadata": {
    "model_used": "llama3.2",
    "generation_time": "float"
  }
}
```

## Behavioral Rules

1.  **Model Constraint**: ALWAYS use `llama3.2` via the internal Ollama instance.
2.  **Templating**: The System Prompt/Template must be stored as a constant/file in the codebase, not hardcoded into the view logic.
3.  **Privacy**: No data leaves the local machine.
4.  **UI Interaction**: The interface behaves like a Chat. User sends text -> System replies with Test Cases.

## Architectural Invariants

1.  **Backend**: Python (FastAPI or simple HTTP server) to bridge UI and Ollama.
2.  **Frontend**: HTML/JS (Vanilla) for the Chat Interface.
3.  **Communication**: JSON over HTTP.

