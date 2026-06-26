from fastapi import APIRouter

from app.services.ai_service import ask_hospital_ai

router = APIRouter()

@router.get("/ask")
def ask(question: str):

    answer = ask_hospital_ai(question)

    return {
        "question": question,
        "answer": answer
    }