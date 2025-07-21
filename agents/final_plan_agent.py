
# agents/final_plan_agent.py
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
ollama_url = os.getenv("OLLAMA_BASE_URL")

def final_plan_node(logger=None):
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def _final_plan_node(state):
        if logger:
            logger("🧩 [Final Planner] Combining all pieces into final plan...")

        prompt = f"""
You are a travel planner AI. Based on the following data, generate a detailed, structured travel itinerary with proper formatting and cost estimate.

- Origin: {state['origin']}
- Dates: {state['start_date']} to {state['end_date']}
- Budget Type: {state['budget_type']}
- Travel Type: {state['travel_type']}
- Preferences: {state['preferences']}
- Destination: {state['destination']}
- Accommodation: {state['accommodation']}
- Food Recommendations: {state['food']}
- Budget Estimate: {state['budget_estimate']}
- Feedback: {state.get('user_feedback', '')}
- Clothing Recommendation: {state.get('clothing_recommendation', '')}


Respond with the complete final travel plan.
"""

        result = llm.invoke(prompt)

        if logger:
            logger("✅ [Final Planner] Final plan generated.")

        return {**state, "final_plan": result.strip()}

    return _final_plan_node
