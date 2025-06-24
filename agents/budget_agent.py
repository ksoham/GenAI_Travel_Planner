from langchain_ollama import OllamaLLM
import os

print("👉 Using Ollama Base URL:", os.getenv("OLLAMA_BASE_URL"))

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)

def budget_node(state):
    prompt = f"""
Estimate a total budget for a trip to {state['destination']} from {state['origin']} for a {state['budget_type']} traveler.
Include travel, accommodation, food, and experiences.
Return total estimate and short breakdown.
"""
    result = llm.invoke(prompt)
    return {**state, "budget_estimate": result.strip()}
