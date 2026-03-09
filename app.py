import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Student Productivity App", page_icon="📚", layout="wide")

# Sidebar
st.sidebar.title("📚 Student Productivity App")
page = st.sidebar.radio("Navigation", ["Home", "Study Planner", "Productivity Tracker", "About"])

st.sidebar.markdown("---")
st.sidebar.info("Simple planner app for students.")

# HOME PAGE
if page == "Home":

    st.title("💜 Welcome to the Student Productivity Planner")

    st.header("Plan your studies and track productivity")

    st.write("This app helps students organize their study schedule.")

    name = st.text_input("Enter your name")

    age = st.number_input("Enter your age", 10, 60)

    subject = st.selectbox(
        "Choose your main subject",
        ["Math", "Science", "Programming", "English", "History"]
    )

    hobbies = st.multiselect(
        "Select your hobbies",
        ["Gaming", "Reading", "Music", "Sports", "Coding"]
    )

    hours = st.slider("How many hours will you study today?", 0, 12)

    reminder = st.checkbox("Enable study reminder")

    color = st.color_picker("Choose your theme color", "#8A2BE2")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Daily Goal", "3 Hours")

    with col2:
        st.metric("Motivation Level", "High")

    if st.button("Save Study Plan"):

        st.success(f"Nice {name}! Your study plan was saved.")

        st.balloons()

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

# STUDY PLANNER
elif page == "Study Planner":

    st.title("📝 Study Planner")

    task = st.text_input("Enter your study task")

    difficulty = st.radio(
        "Task difficulty",
        ["Easy", "Medium", "Hard"]
    )

    duration = st.slider("Estimated time (minutes)", 10, 180)

    date = st.date_input("Study date")

    time_input = st.time_input("Study time")

    uploaded_file = st.file_uploader("Upload your study notes")

    if st.button("Add Task"):

        st.success("Task added successfully!")

    with st.expander("Example Study Plan"):

        data = pd.DataFrame({
            "Subject": ["Math", "Programming", "Science"],
            "Duration": [60, 120, 45]
        })

        st.dataframe(data)

# PRODUCTIVITY TRACKER
elif page == "Productivity Tracker":

    st.title("📊 Productivity Tracker")

    tab1, tab2 = st.tabs(["Daily Rating", "Weekly Chart"])

    with tab1:

        productivity = st.slider("Rate your productivity today", 1, 10)

        focus = st.slider("Focus level", 1, 10)

        if productivity >= 8:

            st.success("Excellent productivity today!")

        elif productivity >= 5:

            st.info("Good job, keep improving!")

        else:

            st.warning("Try to avoid distractions tomorrow.")

    with tab2:

        chart_data = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "Productivity": [5, 7, 6, 8, 9]
        })

        st.bar_chart(chart_data.set_index("Day"))

# ABOUT PAGE
elif page == "About":

    st.title("ℹ About This App")

    st.subheader("What the App Does")

    st.write("""
    The Student Productivity Planner helps students organize their study schedule,
    track productivity levels, and stay motivated.
    """)

    st.subheader("Target Users")

    st.write("""
    The main users are students who want to manage their study time and improve
    their productivity while studying.
    """)

    st.subheader("Inputs Collected")

    st.write("""
    - Name
    - Age
    - Study subjects
    - Study tasks
    - Study hours
    - Productivity ratings
    """)

    st.subheader("Outputs Displayed")

    st.write("""
    - Study plan confirmation
    - Productivity feedback
    - Weekly productivity chart
    - Task tables
    """)

    st.info("This app was created using Streamlit for Assignment 5.")