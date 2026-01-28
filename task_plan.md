# Task Plan

## Phases
- [x] Initialization
- [x] Phase 1: Blueprint (Discovery & Architecture)
- [x] Phase 2: Link (Environment Setup)
- [x] Phase 3: Architect (Core Implementation)
- [x] Phase 4: Stylize (CLI/UI & Formatting)
- [ ] Phase 5: Trigger (Testing & Refinement)






## Goals
- Create a local LLM Testcase generator with Ollama.

## Checklists
- [x] Initialize Project Memory
- [x] **Blueprint**: Collect Discovery Answers
- [ ] **Blueprint**: Receive User Prompt (Template)
- [x] **Blueprint**: Define Schema in `gemini.md`
- [x] **Blueprint**: Create Architecture Diagram/Plan (Architecture defined in task phases)

### Blueprint Summary
- **Architecture**:
    - **Frontend**: Vanilla HTML/JS/CSS (as per your rules) for the Chat Interface.
    - **Backend**: Python (FastAPI) to handle the `PromptTemplate` and communicate with the local Ollama instance.
    - **Database**: None (Stateless/Local).
- **Data Structure**: Rigid JSON output enforcement for test cases.
- **Model**: `llama3.2` running on `localhost`.


### Phase 2: Link (Environment Setup)
- [x] Verify `ollama` is running and `llama3.2`.
- [x] Create `tools/` directory with verification script.
- [x] Run `tools/verify_ollama.py` - Handshake successful.
- [x] Create `backend/` and `frontend/` directories.
- [x] Create `requirements.txt`.


### Phase 3: Architect (Core Implementation)
- [x] Create `architecture/` directory and SOP.
- [x] Create Layer 3 Tools in `tools/` (`ollama_client.py`, `testcase_logic.py`).
- [ ] Create `backend/server.py`: FastAPI app (Layer 2 - Navigation).
- [ ] Create `frontend/` files (Layer 2/4).


### Phase 4: Stylize (CLI/UI & Formatting)
- [x] Create `frontend/style.css` (Premium Glassmorphism).
- [x] Create `frontend/index.html` (Semantic Structure).
- [x] Create `frontend/app.js` (Dynamic UI Rendering).
- [x] Refine JSON Payload display in Frontend.


### Phase 5: Trigger (Testing & Refinement)
- [ ] Test with sample inputs.
- [ ] Validate offline capability.

