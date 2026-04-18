import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Surya's Study Tracker", page_icon="🎓")

# Web Header
st.title("🎓 Smart Study-Budget Tracker")
st.subheader("Developed by M. Surya Teja")
st.write("Optimize your Class 10 prep and your pocket money in one place!")

# Sidebar for Inputs
with st.sidebar:
    st.header("User Details")
    name = st.text_input("Enter your name", "Surya")
    study_hours = st.slider("Hours studied today?", 0.0, 15.0, 5.0)
    money_spent = st.number_input("Money spent on snacks/recharge? (₹)", min_value=0)

# Configuration
TARGET_STUDY_HOURS = 6.0 # Set for Class 10
DAILY_BUDGET_LIMIT = 100.0

# Calculation Logic
efficiency = (study_hours / TARGET_STUDY_HOURS) * 100

# Action Button
if st.button("Calculate My Status"):
    with st.spinner('Analyzing your data...'):
        time.sleep(1) # Keeping your cool delay!
    
    st.divider()
    
    # Results Display
    st.header(f"Results for {name}")
    
    # Efficiency Metric
    st.metric(label="Study Efficiency", value=f"{efficiency:.1f}%", delta=f"{efficiency-100:.1f}% Target")
    
    # Progress Bar
    st.progress(min(efficiency/100, 1.0))

    # Logic Messages
    col1, col2 = st.columns(2)
    
    with col1:
        if efficiency >= 80:
            st.success("🔥 Super Student! On track for Boards.")
        else:
            st.warning("⚠️ Needs Improvement. Focus up!")

    with col2:
        if money_spent > DAILY_BUDGET_LIMIT:
            st.error(f"💸 Over Budget by ₹{money_spent - DAILY_BUDGET_LIMIT}")
        else:
            st.info("✅ Great job saving money!")

    st.balloons() # Celeberation for task completion!