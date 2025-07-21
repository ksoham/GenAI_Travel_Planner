# agents/feedback_agent.py
from langchain_community.llms import Ollama
import os

def feedback_node(logger=None):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    llm = Ollama(model="llama3.1:8b", base_url=ollama_url)

    def node(state):
        if logger:
            logger("🔁 Feedback Agent: Applying feedback to plan...")

        if not state.get("user_feedback"):
            return state  # No feedback to process

        plan = state["final_plan"]
        if len(plan) > 3000:
            plan = plan[:3000] + "\n\n... [truncated]"

        prompt = f"""
You previously created this travel plan:

Plan: {plan}

User feedback: "{state['user_feedback']}"

Revise the plan accordingly and return only the updated itinerary in markdown.
"""
        result = llm.invoke(prompt)
        result_text = result.strip()

        if not result_text:
            if logger:
                logger("⚠️ Feedback Agent: No changes returned by model.")
            return state

        if logger:
            logger("✅ Feedback Agent: Plan revised.")
        return {**state, "final_plan": result_text}

    return node
