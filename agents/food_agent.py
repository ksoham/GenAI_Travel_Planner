# agents/food_agent.py
from langchain_community.llms import Ollama
import os

def food_node(logger=None):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def node(state):
        destination = state.get("destination", "").strip()
        if not destination:
            if logger:
                logger("⚠️ Food Agent: Destination missing. Skipping.")
            return state

        if logger:
            logger("🍽️ Food Agent: Recommending cuisine and local experiences...")

        prompt = f"""
You're a local food expert.

In {destination}, recommend must-try local dishes, snacks, and drinks.
Also suggest 2-3 unique food experiences or street food areas.

Respond in markdown format with categories like:
- 🌮 Must-Try Dishes
- 🍢 Street Food
- 🍴 Food Experiences
"""

        result = llm.invoke(prompt)
        if logger:
            logger("✅ Food Agent: Suggestions complete.")
        return {**state, "food": result.strip()}

    return node
