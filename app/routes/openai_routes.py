from fastapi import APIRouter
from app.services.openai_service import ask_ai

router = APIRouter(
    prefix="/openai",
    tags=["OpenAI"]
)

@router.get("/chat")
async def chat(question: str):
    return {
        "answer": ask_ai(question)
    }