from fastapi import APIRouter
from app.services.embedding_service import get_embedding

router = APIRouter(prefix="/embedding", tags=["Embedding"])

@router.get("/")
def create_embedding(text: str):
    vector = get_embedding(text)

    return {
        "length": len(vector),
        "vector": vector[:10]
    }