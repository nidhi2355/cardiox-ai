from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.llm_service import get_cardio_response

app = FastAPI(title="CardioX AI - Professional Backend")

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def health_check():
    return {"status": "Active", "module": "CardioX-AI"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        # Calls your updated English-centric logic
        response = get_cardio_response(request.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))