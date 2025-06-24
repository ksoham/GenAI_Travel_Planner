from langchain_ollama import OllamaLLM
import os

print("👉 Using Ollama Base URL:", os.getenv("OLLAMA_BASE_URL"))

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)


def accommodation_node(state):
    prompt = f"""
Find suitable accommodation options in {state['destination']} for a {state['budget_type']} traveler.
Dates: {state['start_date']} to {state['end_date']}
Return 2–3 suggestions with short descriptions.
"""
    result = llm.invoke(prompt)
    return {**state, "accommodation": result.strip()}
