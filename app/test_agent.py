from app.services.agent_service import run_agent

question = "What is FastAPI?"

response = run_agent(question)

print(response)