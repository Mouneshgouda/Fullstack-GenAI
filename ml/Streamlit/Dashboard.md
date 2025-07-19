
## Dashboard

```python

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="🌈 Colorful Dashboard", layout="centered")

# Colorful Title with Emojis
st.markdown("<h1 style='color:#6C63FF;'>🌈 My Colorful Dashboard</h1>", unsafe_allow_html=True)
st.caption("📊 Simple stats with a touch of color and style")

# Simulated data
data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Visitors": [120, 135, 90, 160, 180, 200, 150],
    "Sales": [1000, 1100, 950, 1200, 1300, 1400, 1250]
})

# Colored metric cards
st.markdown("### 🔢 Weekly Stats")
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div style='background-color:#FFDEE9;padding:20px;border-radius:10px'><h4>👥 Total Visitors</h4><h2 style='color:#5D3FD3;'>"
                f"{sum(data['Visitors'])}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='background-color:#B5FFFC;padding:20px;border-radius:10px'><h4>💰 Total Sales</h4><h2 style='color:#FF4B4B;'>"
                f"${sum(data['Sales'])}</h2></div>", unsafe_allow_html=True)

# Line chart with subheader
st.markdown("### 📈 Visitors Over the Week")
st.line_chart(data["Visitors"])

# Bar chart
st.markdown("### 📊 Sales Over the Week")
st.bar_chart(data["Sales"])

# Data table with colorful style
st.markdown("### 📋 Weekly Raw Data")
st.dataframe(data.style.background_gradient(cmap='coolwarm'))
```
