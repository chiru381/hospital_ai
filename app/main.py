from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.ai_routes import router as ai_router
from app.routes.embedding_routes import router as embedding_router
from app.routes.qdrant_routes import router as qdrant_router
from app.routes.health_routes import router as health_router
from app.services.qdrant_service import create_collection
from app.services.rag_service import ingest_pdfs
from app.routes.document_routes import (
    router as document_router
)

app = FastAPI()

app.include_router(document_router)

@app.on_event("startup")


async def startup():
    create_collection()
    
    ingest_pdfs()

    print("Hospital PDFs loaded")
    

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

app.include_router(
    ai_router,
    prefix="/ai"
)

app.include_router(user_router)
app.include_router(embedding_router)
app.include_router(qdrant_router)
app.include_router(health_router)

# http://127.0.0.1:8000/ai/chat?question=What%20is%20FastAPI
# http://127.0.0.1:8000/ai/ask?question=What%20is%20my%20company%20name
# http://127.0.0.1:8000/ai/agent?question=What%20is%20FastAPI
# http://127.0.0.1:8000/embedding/?text=Hello%20World
# http://127.0.0.1:8000/search/
