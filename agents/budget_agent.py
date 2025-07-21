
# budget_agent.py
from langchain_community.llms import Ollama
import os

def budget_node(logger=None):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def node(state):
        if logger:
            logger("💸 Budget Agent: Estimating total trip budget...")
        prompt = f"""
Estimate the total travel budget for a {state['budget_type']} trip from {state['origin']} to {state['destination']} from {state['start_date']} to {state['end_date']}. Include costs for:

- Travel
- Accommodation
- Food
- Experiences
Respond with a range (e.g. ₹40,000 – ₹60,000) and a brief breakdown.
"""
        result = llm.invoke(prompt)
        if logger:
            logger("✅ Budget Agent: Estimate complete.")
        return {**state, "budget_estimate": result.strip()}

    return node
