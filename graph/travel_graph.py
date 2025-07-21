# travel_graph.py
from langgraph.graph import StateGraph
from typing import TypedDict

from agents.destination_agent import destination_node
from agents.accommodation_agent import accommodation_node
from agents.food_agent import food_node
from agents.budget_agent import budget_node
from agents.itinerary_agent import itinerary_node
from agents.feedback_agent import feedback_node
from agents.final_plan_agent import final_plan_node
from agents.clothing_agent import clothing_node

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
    clothing_recommendation: str

def build_travel_graph(logger=None):
    builder = StateGraph(TripState)

    builder.add_node("destination_agent", destination_node(logger))
    builder.add_node("accommodation_agent", accommodation_node(logger))
    builder.add_node("food_agent", food_node(logger))
    builder.add_node("budget_agent", budget_node(logger))
    builder.add_node("itinerary_agent", itinerary_node(logger))
    builder.add_node("clothing_agent", clothing_node(logger))  # 👈 must come before final_plan
    builder.add_node("final_plan_agent", final_plan_node(logger))
    builder.add_node("feedback_agent", feedback_node(logger))

    builder.set_entry_point("destination_agent")
    builder.add_edge("destination_agent", "accommodation_agent")
    builder.add_edge("accommodation_agent", "food_agent")
    builder.add_edge("food_agent", "budget_agent")
    builder.add_edge("budget_agent", "itinerary_agent")
    builder.add_edge("itinerary_agent", "clothing_agent")
    builder.add_edge("clothing_agent", "final_plan_agent")
    builder.add_edge("final_plan_agent", "feedback_agent")

    return builder.compile()
