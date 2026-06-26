from ollama import embeddings
from app.utils.logger import logger

logger.info("Creating embedding")
def get_embedding(text: str):
    response = embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response["embedding"]