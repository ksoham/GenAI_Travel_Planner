from langchain_ollama import OllamaLLM
import os

print("👉 Using Ollama Base URL:", os.getenv("OLLAMA_BASE_URL"))

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)


def destination_node(state):
    prompt = f"""
Suggest a travel destination for a trip from {state['origin']} between {state['start_date']} and {state['end_date']}.
Budget: {state['budget_type']}
Type: {state['travel_type']}
Preferences: {state['preferences']}
Return just destination and a short explanation.
"""
    result = llm.invoke(prompt)
    return {**state, "destination": result.strip()}
