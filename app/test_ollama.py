from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    request_timeout=120
)

response = llm.invoke("What is FastAPI?")

print(response.content)