# accommodation_agent.py
from langchain_community.llms import Ollama
import os

def accommodation_node(logger=None):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def node(state):
        if logger:
            logger("🏨 Accommodation Agent: Fetching accommodation options...")
        prompt = f"""
Recommend accommodations in {state['destination']} for a {state['budget_type']} trip.
List 2-3 hotels with approximate nightly prices.
"""
        result = llm.invoke(prompt)
        if logger:
            logger("✅ Accommodation Agent: Recommendations complete.")
        return {**state, "accommodation": result.strip()}

    return node
