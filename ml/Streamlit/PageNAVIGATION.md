
## Page NAVIGATION

```python
import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(page_title="Single-Page Multi-Page App", layout="wide")

# ---------------------------
# SIDEBAR NAVIGATION
# ---------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📄 About", "📊 Charts", "📞 Contact"])

# ---------------------------
# HOME PAGE
# ---------------------------
if page == "🏠 Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the **Home Page** of this single-page Streamlit app!")
    st.success("Use the sidebar to navigate to different sections.")

# ---------------------------
# ABOUT PAGE
# ---------------------------
elif page == "📄 About":
    st.title("📄 About Page")
    st.write("This is the About Page.")
    st.markdown("""
    **Features in this app:**
    - Sidebar Navigation
    - Multiple Pages in a Single File
    - Charts, Tables, and Forms
    """)

# ---------------------------
# CHARTS PAGE
# ---------------------------
elif page == "📊 Charts":
    st.title("📊 Charts Page")

    st.subheader("Random Data Chart")
    data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    st.line_chart(data)

    st.subheader("Area Chart")
    st.area_chart(data)

    st.subheader("Data Table")
    st.table(data.head())

# ---------------------------
# CONTACT PAGE
# ---------------------------
elif page == "📞 Contact":
    st.title("📞 Contact Page")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you {name}, we have received your message!")

```
