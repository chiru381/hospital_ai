from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    request_timeout=120
)

def ask_ai(question: str):
    try:
        response = llm.invoke(question)

        if hasattr(response, "content"):
            return response.content

        return str(response)

    except Exception as e:
        return f"Error: {str(e)}"