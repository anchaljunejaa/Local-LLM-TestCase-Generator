# Findings

## Research
- [x] **Ollama Integration**: The `ollama` Python library is the standard way to interact with local models. Key functions: `ollama.generate()` (one-shot) and `ollama.chat()` (conversational).
- [x] **Test Case Generation**: Strategies include providing source code + function descriptions + existing test examples in the prompt.
- [x] **Models**: Common models for this are `llama3`, `codellama`, or `mistral`. 

## Discoveries
- **Offline Capability**: Entire system can run offline, ensuring privacy for codebases.
- **Cost**: Zero inference cost using local compute.

## Constraints
- **Hardware**: performance depends on user's GPU/RAM.
- **Model Context Window**: Limited context size might be an issue for very large files; we may need to chunk inputs.

