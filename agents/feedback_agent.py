from langchain_ollama import OllamaLLM
import os

llm = OllamaLLM(
    model="llama3.1:8b",
    base_url=os.getenv("OLLAMA_BASE_URL")
)

def feedback_node(state):
    if "user_feedback" not in state or not state["user_feedback"].strip():
        return state  # Skip if no feedback given

    prompt = f"""
You previously created this travel plan:

Plan: {state['final_plan']}

User feedback: "{state['user_feedback']}"

Revise the plan accordingly and return only the updated itinerary in markdown.
"""
    revised = llm.invoke(prompt)
    return {**state, "final_plan": revised.strip()}
