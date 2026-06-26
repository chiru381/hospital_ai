from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.services.embedding_service import get_embedding
from app.utils.chunking import split_text
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from app.utils.logger import logger
import os
import uuid
sample = get_embedding("hello")

logger.info("Connecting to Qdrant")

load_dotenv()

client = QdrantClient(
    host=os.getenv("QDRANT_HOST"),
    port=int(os.getenv("QDRANT_PORT"))
)

COLLECTION_NAME = os.getenv("QDRANT_COLLECTION")

def create_collection():

    collections = client.get_collections()

    existing = [
        c.name
        for c in collections.collections
    ]

    if COLLECTION_NAME not in existing:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=len(sample),
                distance=Distance.COSINE
            )
        )



def insert_document(text: str):

    chunks = split_text(text)

    points = []

    for chunk in chunks:

        vector = get_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def search_documents(query: str):
    query_vector = get_embedding(query)

    print("Embedding length:", len(query_vector))

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    )

    return [
        {
            "id": point.id,
            "score": point.score,
            "payload": point.payload
        }
        for point in results.points
    ]