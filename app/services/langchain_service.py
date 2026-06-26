from app.services.rag_service import retrieve_context
from app.services.openai_service import llm


def ask_rag(question: str):

    context = retrieve_context(question)

    prompt = f"""
    You are a helpful assistant.

    Use ONLY the provided context.

    If answer is not present in context,
    reply:

    "I don't know based on the provided documents."

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content