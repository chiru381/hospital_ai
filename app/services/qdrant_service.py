from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(
    host="localhost",
    port=6333
)

COLLECTION_NAME = "hospital_knowledge"

def create_collection():

    collections = client.get_collections()

    names = [c.name for c in collections.collections]

    if COLLECTION_NAME not in names:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=768,      # <-- CHANGE TO 768
                distance=Distance.COSINE
            )
        )