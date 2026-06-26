# agent_routes.py

from fastapi import APIRouter
from app.services.agent_service import run_agent

router = APIRouter(
    prefix="/agent",
    tags=["Agent"]
)

@router.get("/")
async def ask_agent(question: str):
    return {
        "answer": run_agent(question)
    }