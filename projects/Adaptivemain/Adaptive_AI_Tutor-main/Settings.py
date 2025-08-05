# pages/Settings.py
import streamlit as st
from utils.session_manager import load_user_profile, save_user_profile

def run():
    st.title("⚙️ Settings - Edit Subjects & Marks")

    username = st.text_input("Enter your name to update your profile:")

    if not username:
        return

    profile = load_user_profile(username)
    if not profile:
        st.error("Profile not found.")
        return

    st.success(f"Editing profile for {username}")

    new_subjects = {}
    num = st.number_input("How many subjects do you want to enter?", 1, 20, len(profile['grades']))

    with st.form("edit_form"):
        for i in range(int(num)):
            col1, col2 = st.columns(2)
            with col1:
                subject = st.text_input(f"Subject {i + 1}:", value=list(profile["grades"].keys())[i] if i < len(profile["grades"]) else "", key=f"subject_{i}")
            with col2:
                marks = st.slider(f"Marks for {subject}:", 0, 100, value=profile["grades"].get(subject, 75), key=f"marks_{i}")

            if subject:
                new_subjects[subject] = marks

        submit = st.form_submit_button("Update Profile")

        if submit:
            profile["grades"] = new_subjects
            profile["subjects"] = list(new_subjects.keys())
            save_user_profile(username, profile)
            st.success("Profile updated successfully!")
