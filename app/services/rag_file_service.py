from app.services.embedding_service import get_embedding
from app.services.qdrant_service import client, COLLECTION_NAME

def retrieve_context(query: str):

    query_vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    )

    return "\n".join(
        [
            point.payload["text"]
            for point in results.points
        ]
    )