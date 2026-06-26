from fastapi import APIRouter

from app.services.rag_service import ingest_pdfs

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post("/ingest")
def ingest():

    return {
        "message": ingest_pdfs()
    }