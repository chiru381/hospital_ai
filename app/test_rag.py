from app.services.langchain_service import ask_rag

question = "What is FastAPI?"

response = ask_rag(question)

print(response)