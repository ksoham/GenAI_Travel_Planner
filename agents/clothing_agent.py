# agents/clothing_agent.py
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
ollama_url = os.getenv("OLLAMA_BASE_URL")

def clothing_node(logger=None):
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def _clothing_node(state):
        if logger:
            logger("🧥 [Clothing Agent] Recommending clothing for the trip...")

        prompt = f"""
You are a fashion stylist AI assistant.

Suggest appropriate travel clothing for both men and women based on:
- Destination: {state['destination']}
- Travel dates: {state['start_date']} to {state['end_date']}
- Travel type: {state['travel_type']} (e.g., romantic, adventure)
- Budget type: {state['budget_type']}
- Preferences: {state['preferences']}

List daywear, evening wear, footwear, and accessories for both men and women separately.
Keep the suggestions stylish but realistic and suitable for the destination’s culture and climate.
"""

        response = llm.invoke(prompt)

        if logger:
            logger("✅ [Clothing Agent] Clothing recommendations ready.")

        return {**state, "clothing_recommendation": response.strip()}

    return _clothing_node
