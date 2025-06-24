from langchain_ollama import OllamaLLM
import os

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)

def itinerary_node(state):
    prompt = f"""
You're a travel itinerary expert. Given this destination and preferences, create a detailed day-wise plan.

Destination: {state['destination']}
Dates: {state['start_date']} to {state['end_date']}
Preferences: {state['preferences']}
Include 3–5 activities per day and short descriptions.

Return the itinerary as markdown.
"""
    result = llm.invoke(prompt)
    return {**state, "final_plan": result.strip()}
