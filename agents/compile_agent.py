from langchain_ollama import OllamaLLM
import os

print("👉 Using Ollama Base URL:", os.getenv("OLLAMA_BASE_URL"))

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)

def compile_node(state):
    prompt = f"""
Create a final travel plan with the following:
- Destination: {state['destination']}
- Accommodation: {state['accommodation']}
- Food: {state['food']}
- Budget: {state['budget_estimate']}

Write a nice summary as if giving a travel itinerary.
"""
    result = llm.invoke(prompt)
    return {**state, "final_plan": result.strip()}
