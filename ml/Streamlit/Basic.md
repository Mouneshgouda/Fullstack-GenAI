## 🧱 Step 1: What is Streamlit?
- Streamlit is a Python library that lets you turn scripts into web apps with zero frontend code.

- You can use it for:

- 📊 Dashboards

- 🤖 Machine Learning demos

- 📦 Product recommendation tools

- 🧪 Data science experiments

## 🛠️ Step 2: Install Streamlit
Make sure you have Python installed. Then run:

- pip install streamlit
- streamlit hello
- It will launch a demo app in your browser.

## 📂 Step 3: Create Your First App
- Open any folder.

- Create a file: app.py
```python
import streamlit as st
st.title("👋 Hello Streamlit!")
st.write("This is your first Streamlit app.")
##run 
streamlit run app.py
```
## 🧩 Step 4: Learn Basic Components
```python
st.title()	Big title at the top	      st.title("Welcome")
st.write()	Display text or objects	      st.write("Hello!")
st.text_input()	Input box	              name = st.text_input("Name")
st.button()	Clickable button	          st.button("Submit")
st.slider()	Select a number	              age = st.slider("Age", 0, 100)
st.checkbox()	True/False toggle	      if st.checkbox("Show"):
st.balloons()	Fun balloons animation	  st.balloons()
st.line_chart()	Create a line chart	      st.line_chart([1,2,3,4])
```

## 🔄 Step 5: Add Interactivity
```python 
import streamlit as st

name = st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"Hello, {name}!")
```

    
## 📈 Step 6: Plot a Chart
```python
import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)
```

## 🧊 Step 7: Use Fun Effects
```python
import streamlit as st

if st.button("Celebrate!"):
    st.balloons()

if st.button("Let it snow ❄️"):
    st.snow()
```
