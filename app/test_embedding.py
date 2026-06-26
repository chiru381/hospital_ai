from app.services.embedding_service import get_embedding

vector = get_embedding("What is FastAPI")

print("Vector Length:", len(vector))
print(vector[:10])  # first 10 values