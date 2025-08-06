#  Course Recommender

# app.py
```python

import streamlit as st
import requests
import base64

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set background from local image
def set_background(image_file):
    img_base64 = get_base64_image(image_file)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#  Set your image path here (same folder or subfolder like ./assets/bg.jpg)
set_background("background-blur-clean-531880.jpg")

# Streamlit UI
st.title("🎓 Course Recommender")
st.write("Get similar courses from the Coursera dataset")

# User input
course_name = st.text_input("Enter course name (exactly as in dataset):")
num_recs = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Get Recommendations"):
    if not course_name:
        st.warning("Please enter a course name.")
    else:
        url = "http://localhost:8000/recommend"
        params = {"course_name": course_name, "num_recommendations": num_recs}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, str):
                st.error(data)
            else:
                st.success("Recommendations:")
                for course in data:
                    st.markdown(f"{course['Course Name']}")
                    st.write(f"University: {course['University']}")
                    st.write(f"Rating: {course['Course Rating']}")
                    st.markdown(f"[Go to Course]({course['Course URL']})")
                    st.markdown("---")
        else:
            st.error("Failed to get recommendations.")

```
## main.py

```python
from fastapi import FastAPI, Query
from typing import List, Union
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load saved components
df = joblib.load("courses_df.pkl")
cosine_sim = joblib.load("cosine_sim.pkl")
indices = joblib.load("indices.pkl")

app = FastAPI(title="Course Recommender API")

@app.get("/recommend")
def recommend_courses(course_name: str = Query(...), num_recommendations: int = Query(5)) -> Union[List[dict], str]:
    if course_name not in indices:
        return f"Course '{course_name}' not found."

    idx = indices[course_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    course_indices = [i[0] for i in sim_scores]

    recommendations = df[['Course Name', 'University', 'Course Rating', 'Course URL']].iloc[course_indices]
    return recommendations.to_dict(orient='records')

```
