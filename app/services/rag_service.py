import uuid

from app.services.embedding_service import get_embedding

from app.services.qdrant_service import (
    client,
    COLLECTION_NAME
)

from app.services.document.pdf_service import load_all_pdfs

from app.utils.chunking import split_text
from qdrant_client.models import Filter
from app.utils.constants import PDF_FOLDER


def ingest_pdfs():
    client.delete(
        collection_name=COLLECTION_NAME,
        points_selector=Filter()
    )

    docs = load_all_pdfs(PDF_FOLDER)

    for doc in docs:

        chunks = split_text(doc["content"])

        for chunk in chunks:

            embedding = get_embedding(chunk)
            print("Embedding Length =", len(embedding))

            client.upsert(
                collection_name=COLLECTION_NAME,
                points=[
                    {
                        "id": str(uuid.uuid4()),
                        "vector": embedding,
                        "payload": {
                            "source": doc["file"],
                            "text": chunk
                        }
                    }
                ]
            )

    return "PDF ingestion completed"



def search_documents(question):

    vector = get_embedding(question)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=5
    )

    return [
        {
            "source": point.payload["source"],
            "text": point.payload["text"]
        }
        for point in results.points
    ]