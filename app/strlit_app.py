import os
import sys
from dotenv import load_dotenv
from datetime import datetime
import streamlit as st

# Load environment variables
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graph.travel_graph import build_travel_graph

# Streamlit page config
st.set_page_config(page_title="🧠 GenAI Travel Planner", layout="wide")
st.title("🧠 GenAI Travel Planner")

# -- Sidebar: User Inputs
with st.sidebar:
    st.header("📋 Trip Details")
    origin = st.text_input("🌍 Origin", "Mumbai")
    start = st.date_input("📅 Start Date", datetime.today())
    end = st.date_input("📅 End Date")
    budget = st.selectbox("💰 Budget", ["cheap", "moderate", "luxury"])
    travel_type = st.selectbox("🎒 Type", ["relaxing", "adventure", "cultural", "romantic"])
    prefs = st.text_area("💭 Preferences", "beach, food")

# -- Mermaid Visualization
st.markdown("### 🧩 Multi-Agent Orchestration Flow")
st.markdown("""
```mermaid
graph TD;
    UserInput[User Input] --> MainPlanner(Main Planner)
    MainPlanner --> DestinationAgent
    DestinationAgent --> AccommodationAgent
    AccommodationAgent --> FoodAgent
    FoodAgent --> BudgetAgent
    BudgetAgent --> ItineraryAgent
    ItineraryAgent --> FeedbackAgent
    FeedbackAgent --> FinalPlanAgent
    FinalPlanAgent --> FinalOutput[Final Plan]
""")
# -- Initialize Session State
if "last_plan" not in st.session_state:
    st.session_state.last_plan = ""
if "state" not in st.session_state:
    st.session_state.state = {}
# -- Generate Plan
if st.button("🧠 Generate Plan"):
    # Initialize state
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
    st.session_state.state = state

    # Show spinner and logs
    with st.spinner("Planning your perfect trip..."):
        st.markdown("#### 🛠️ Execution Log")
        log_area = st.empty()
        log_history = []


        def log(msg):
            log_history.append(msg)
            log_area.text("\n".join(log_history))


        log("🚀 Sending input to Main Planner Agent...")

        # Build and run graph
        graph = build_travel_graph(logger=log)
        result = graph.invoke(state)

        # Store and display final plan
        st.session_state.last_plan = result["final_plan"]
        st.session_state.state = result

    st.markdown("### 🗺 Final Plan:")
    st.markdown(st.session_state.last_plan)

# -- Feedback & Revision
if st.session_state.last_plan:
    st.markdown("---")
    st.markdown("### 📝 Provide Feedback to Refine Plan")
    feedback = st.text_area("💬 What would you like to change or improve?", "")
    if st.button("🔁 Revise Plan"):
        st.session_state.state["user_feedback"] = feedback
        with st.spinner("Applying your feedback..."):
            graph = build_travel_graph(logger=log)
            revised_result = graph.invoke(st.session_state.state)
            st.session_state.last_plan = revised_result["final_plan"]
            st.session_state.state = revised_result

        st.markdown("### 🔄 Revised Plan:")
        st.markdown(st.session_state.last_plan)




