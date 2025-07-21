# agents/itinerary_agent.py
from langchain_community.llms import Ollama
import os

def itinerary_node(logger=None):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def node(state):
        destination = state.get("destination", "").strip()
        start_date = state.get("start_date", "").strip()
        end_date = state.get("end_date", "").strip()

        if not destination or not start_date or not end_date:
            if logger:
                logger("⚠️ Itinerary Agent: Missing critical trip details. Skipping.")
            return state

        if logger:
            logger("🗓️ Itinerary Agent: Creating day-wise itinerary...")

        prompt = f"""
You're a travel itinerary expert. Given the details below, generate a detailed, engaging day-wise travel plan.

Destination: {destination}
Dates: {start_date} to {end_date}
Preferences: {state.get('preferences', 'None provided')}

Include 3–5 activities per day with short descriptions.
Format the response in **markdown** with headers for each day.
"""

        result = llm.invoke(prompt)

        if logger:
            logger("✅ Itinerary Agent: Plan created.")

        return {**state, "itinerary": result.strip()}

    return node
