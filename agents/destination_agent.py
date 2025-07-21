# agents/destination_agent.py
import os
from langchain_community.llms import Ollama

def destination_node(logger=None):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def node(state):
        if logger:
            logger("📍 Destination Agent: Received input and generating destination...")

        prompt = f"""
Suggest a travel destination for a trip from {state['origin']} between {state['start_date']} and {state['end_date']}.
Budget: {state['budget_type']}
Type: {state['travel_type']}
Preferences: {state['preferences']}
Return just the destination and a short explanation.
"""
        result = llm.invoke(prompt)

        if logger:
            logger("✅ Destination Agent: Completed with result.")

        return {**state, "destination": result.strip()}

    return node
