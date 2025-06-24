from langchain_ollama import OllamaLLM
import os

print("👉 Using Ollama Base URL:", os.getenv("OLLAMA_BASE_URL"))

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)

def food_node(state):
    prompt = f"""
List must-try foods and local experiences in {state['destination']} based on the travel type {state['travel_type']} and preferences {state['preferences']}.
Give a bullet list of 3–5 suggestions.
"""
    result = llm.invoke(prompt)
    return {**state, "food": result.strip()}
