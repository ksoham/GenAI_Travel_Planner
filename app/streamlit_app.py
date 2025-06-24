from dotenv import load_dotenv
load_dotenv()
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("travel_planner")

import sys
import os
print("👉 OLLAMA_BASE_URL:", os.getenv("OLLAMA_BASE_URL"))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from graph.travel_graph import build_travel_graph

st.set_page_config(page_title="🧠 GenAI Travel Planner", layout="wide")
st.title("🧠 GenAI Travel Planner")

# User Inputs
origin = st.text_input("🌍 Origin", "Mumbai")
start = st.date_input("📅 Start Date")
end = st.date_input("📅 End Date")
budget = st.selectbox("💰 Budget", ["cheap", "moderate", "luxury"])
travel_type = st.selectbox("🎒 Type", ["relaxing", "adventure", "cultural", "romantic"])
prefs = st.text_area("💭 Preferences", "city explore, historic")

# Session state to store original result
if "last_plan" not in st.session_state:
    st.session_state.last_plan = None
    st.session_state.state = {}

# Generate Plan
if st.button("🚀 Generate Plan"):
    state = {
        "origin": origin,
        "start_date": str(start),
        "end_date": str(end),
        "budget_type": budget,
        "travel_type": travel_type,
        "preferences": prefs,
        "destination": "",
        "accommodation": "",
        "food": "",
        "budget_estimate": "",
        "final_plan": "",
        "user_feedback": ""
    }
    with st.spinner("Planning your trip..."):
        graph = build_travel_graph()
        result = graph.invoke(state)
        st.session_state.last_plan = result["final_plan"]
        st.session_state.state = result

    st.markdown("### 🗺 Final Plan:")
    st.markdown(st.session_state.last_plan)

# Feedback & Revision
# Feedback & Revision
if st.session_state.get("last_plan"):
    st.markdown("---")
    st.markdown("### 📝 Provide Feedback to Refine Plan")
    feedback = st.text_area("💬 What would you like to change?", "")

    if st.button("🔁 Revise Plan"):
        st.session_state.state["user_feedback"] = feedback
        with st.spinner("Revising your plan based on feedback..."):
            graph = build_travel_graph()
            revised_result = graph.invoke(st.session_state.state)
            st.session_state.last_plan = revised_result["final_plan"]
            st.session_state.state = revised_result

        st.markdown("### 🔄 Revised Plan:")
        st.markdown(st.session_state.last_plan)

