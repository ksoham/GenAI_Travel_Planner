# travel_graph.py
from langgraph.graph import StateGraph
from typing import TypedDict

from agents.destination_agent import destination_node
from agents.accommodation_agent import accommodation_node
from agents.food_agent import food_node
from agents.budget_agent import budget_node
from agents.itinerary_agent import itinerary_node
from agents.feedback_agent import feedback_node

class TripState(TypedDict):
    origin: str
    start_date: str
    end_date: str
    budget_type: str
    travel_type: str
    preferences: str
    destination: str
    accommodation: str
    food: str
    budget_estimate: str
    final_plan: str
    user_feedback: str

def build_travel_graph():
    builder = StateGraph(TripState)

    builder.add_node("destination_agent", destination_node)
    builder.add_node("accommodation_agent", accommodation_node)
    builder.add_node("food_agent", food_node)
    builder.add_node("budget_agent", budget_node)
    builder.add_node("itinerary_agent", itinerary_node)
    builder.add_node("feedback_agent", feedback_node)

    builder.set_entry_point("destination_agent")
    builder.add_edge("destination_agent", "accommodation_agent")
    builder.add_edge("accommodation_agent", "food_agent")
    builder.add_edge("food_agent", "budget_agent")
    builder.add_edge("budget_agent", "itinerary_agent")
    builder.add_edge("itinerary_agent", "feedback_agent")

    return builder.compile()