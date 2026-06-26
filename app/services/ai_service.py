import ollama

from app.services.rag_service import search_documents

from app.utils.prompts import HOSPITAL_PROMPT


def ask_hospital_ai(question):

    context = search_documents(question)

    prompt = f"""
    {HOSPITAL_PROMPT}

    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]