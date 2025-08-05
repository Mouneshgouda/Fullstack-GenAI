import streamlit as st
import os
import Home, Performance, Settings

st.set_page_config(page_title="Adaptive AI Tutor", layout="centered")
st.title("Adaptive AI Tutor")
tab_titles = ["Home", "Performance", "Settings"]
tabs = st.tabs(tab_titles)

with tabs[0]:
    st.title("Home")
    Home.run()

with tabs[1]:
    Performance.run()
    
with tabs[2]:
    Settings.run()