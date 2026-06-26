from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

client = QdrantClient(
    host="localhost",
    port=6333
)

COLLECTION_NAME = "hospital_documents"


def save_vectors(chunks, vectors):

    points = []

    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):

        points.append(

            PointStruct(

                id=i,

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