# SOP: Local LLM Testcase Generator

## Goal
Generate deterministic, high-quality test cases from user-provided software requirements using a local LLM (llama3.2 via Ollama).

## Input
- `user_input`: A string containing the feature description or software requirement.
- `output_format`: JSON (as confirmed by the user).

## Process Logic
1. **Validation**: Ensure the input is not empty.
2. **Preprocessing**: Wrap the user input in a "Mission-Specific" prompt template designed for test case generation.
3. **LLM Execution**: Send the prompt to the local Ollama instance using the `llama3.2` model.
4. **Post-processing**:
    - Extract JSON from the LLM response.
    - Validate that the JSON conforms to the expected schema.
5. **Output**: Return the validated JSON object to the frontend.

## Tool Logic (Layer 3)
- `tools/ollama_client.py`: A script that handles communication with the Ollama local API.
- `tools/json_validator.py`: A script to ensure the LLM output is valid JSON and matches the required schema.

## Edge Cases
- **Ollama Offline**: Tool must return a specific error if the Ollama service is not reachable.
- **Model Missing**: Tool must check if `llama3.2` is pulled and available.
- **Malformed JSON**: If the LLM returns invalid JSON, a "retry" or "cleaning" logic should be applied.
- **Empty Input**: System should reject empty strings immediately.
