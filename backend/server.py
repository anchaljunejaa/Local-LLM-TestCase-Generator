from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from tools.testcase_logic import generate_testcases
import uvicorn
import os

app = FastAPI()

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class RequirementRequest(BaseModel):
    requirement: str

@app.post("/generate")
async def process_requirement(req: RequirementRequest):
    """
    Endpoint (Layer 2 - Navigation)
    Routes the requirement to the Layer 3 testcase logic tool.
    """
    result = generate_testcases(req.requirement)
    
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
        
    return result

# Serve static frontend files
if os.path.exists("frontend"):
    app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
