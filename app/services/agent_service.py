from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3"
)

def search_documents(query: str):
    return f"Found information about: {query}"

def run_agent(question: str):

    context = search_documents(question)

    prompt = f"""
    Use this information:

    {context}

    Answer:

    {question}
    """

    response = llm.invoke(prompt)

    return response.content