from fastapi import APIRouter
from app.services.langchain_service import ask_rag

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

@router.get("/")
async def rag(question: str):

    answer = ask_rag(question)

    return {
        "question": question,
        "answer": answer
    }