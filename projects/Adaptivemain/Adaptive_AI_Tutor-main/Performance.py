# pages/Performance.py
import streamlit as st
from utils.session_manager import load_user_profile

def run():
    st.title("📊 Your Performance")

    username = st.text_input("Enter your name to view performance:")

    if not username:
        return

    profile = load_user_profile(username)
    if not profile:
        st.error("User not found.")
        return

    st.success(f"Performance of {username}")
    progress = profile.get("progress", {})

    if not progress:
        st.info("No quiz data available yet.")
        return

    for subject, history in progress.items():
        st.subheader(subject)
        if not history:
            st.text("No records yet.")
            continue

        for idx, result in enumerate(history, 1):
            st.write(f"Quiz {idx}: Score: {result['score']}%")

