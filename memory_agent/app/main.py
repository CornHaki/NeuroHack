from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.agent import MemoryAgent

app = FastAPI(title="NeuroHack Memory Agent")
agent = MemoryAgent()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        result = agent.process_message(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memories")
async def get_all_memories():
    return agent.memory_store.get_all_memories()

