from fastapi import APIRouter
from app.services.rag_service import search_documents

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("/")
def search(query: str):

    results = search_documents(query)

    return {
        "query": query,
        "results": results
    }