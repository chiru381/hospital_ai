from fastapi import APIRouter
from app.services.openai_service import ask_ai
from app.services.langchain_service import ask_rag
from app.services.agent_service import run_agent

router = APIRouter(
    tags=["AI"]
)

@router.get("/agent")
def agent(question: str):

    answer = run_agent(question)

    return {
        "answer": answer
    }

@router.get("/ask")
def ask(question: str):

    answer = ask_rag(question)

    return {
        "question": question,
        "answer": answer
    }

@router.get("/chat")
async def chat(question: str):

    answer = ask_ai(question)

    return {
        "question": question,
        "answer": answer
    }