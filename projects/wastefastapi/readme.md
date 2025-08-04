## Fastapi and streamlit
### main.py

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Allow Streamlit frontend (running on localhost:8501)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production: specify Streamlit origin
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load model
model = load_model("modelnew.h5")

labels = {
    0: "cardboard",
    1: "glass",
    2: "metal",
    3: "paper",
    4: "plastic",
    5: "trash"
}

def preprocess(img: Image.Image):
    img = img.resize((300, 300))
    img_array = np.array(img) / 255.0
    return img_array[np.newaxis, ...]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    processed = preprocess(image)
    prediction = model.predict(processed)
    class_index = int(np.argmax(prediction[0]))
    confidence = float(np.max(prediction[0])) * 100

    return {
        "predicted_class": labels[class_index],
        "confidence": round(confidence, 2)
    }
```

## app.py

```python

import streamlit as st
import requests
from PIL import Image
import io

# Title
st.title("Smart Garbage Segregation")

# Upload file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Send image to FastAPI backend
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/predict/", files=files)

        if response.status_code == 200:
            result = response.json()
            st.subheader("Prediction Result")
            st.write(f"*Predicted Class:* {result['predicted_class']}")
            st.write(f"*Confidence:* {result['confidence']}%")
        else:
            st.error("Prediction failed. Check FastAPI server.")
```



## Index.html
```python
<!DOCTYPE html>
<html>
<head>
    <title>Smart Garbage Segregation</title>
    <link rel="stylesheet" href="/static/styles.css">

</head>
<body>
    <h1>Smart Garbage Segregation</h1>
    <form action="/predict/" method="post" enctype="multipart/form-data">
        <label>Select an image:</label><br><br>
        <input type="file" name="file" accept="image/*" required><br><br>
        <button type="submit">Predict</button>
    </form>

    <p>
        After submitting, the JSON result (with predicted class and confidence) will be shown in the browser.
    </p>
</body>
</html>

```
## result.html

```python
<!DOCTYPE html>
<html>
<head>
    <title>Prediction Result</title>
    <link rel="stylesheet" href="/static/styles.css">

</head>
<body>
    <h2>Prediction Result</h2>
    <img src="{{ image_url }}" alt="Uploaded Image" width="300"><br><br>

    <p><strong>Predicted Class:</strong> {{ predicted_class }}</p>
    <p><strong>Confidence:</strong> {{ probability }}%</p>

    <a href="/">Try another image</a>
</body>
</html>
```

## app.py

```python
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io
import os
from uuid import uuid4

app = FastAPI()

# Mount static directories
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Load the model
model = load_model("modelnew.h5")

# Labels
labels = {
    0: "cardboard",
    1: "glass",
    2: "metal",
    3: "paper",
    4: "plastic",
    5: "trash"
}

# Ensure uploads folder exists
os.makedirs("uploads", exist_ok=True)

# Preprocessing function
def preprocess(img: Image.Image):
    img = img.resize((300, 300))
    img_array = np.array(img, dtype='uint8') / 255.0
    return img_array[np.newaxis, ...]

# Route to render the form using a Jinja2 template
@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction route
@app.post("/predict/", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    processed_img = preprocess(img)

    prediction = model.predict(processed_img)
    pred_index = int(np.argmax(prediction[0]))
    pred_class = labels[pred_index]
    probability = round(float(np.max(prediction[0])) * 100, 2)

    # Save uploaded image
    filename = f"{uuid4().hex}_{file.filename}"
    filepath = os.path.join("uploads", filename)
    with open(filepath, "wb") as buffer:
        buffer.write(contents)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "predicted_class": pred_class,
        "probability": probability,
        "image_url": f"/uploads/{filename}"
    })

```

## styles.css

```python

/* styles.css */

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(to right, #141e30, #243b55);
    color: #fff;
    text-align: center;
    padding: 50px;
    margin: 0;
    animation: fadeIn 1s ease-in;
}

h1, h2 {
    font-size: 2.5em;
    margin-bottom: 30px;
}

form {
    background-color: rgba(255, 255, 255, 0.07);
    padding: 30px;
    border-radius: 10px;
    display: inline-block;
    animation: zoomIn 0.8s ease-out;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

input[type="file"] {
    margin: 15px 0;
    font-size: 1em;
    background-color: #fff;
    color: #000;
    padding: 8px;
    border-radius: 5px;
}

button {
    background-color: #00c853;
    color: white;
    border: none;
    padding: 10px 25px;
    font-size: 1em;
    cursor: pointer;
    border-radius: 5px;
    transition: transform 0.3s ease;
    animation: pulse 2s infinite;
}

button:hover {
    background-color: #00e676;
    transform: scale(1.05);
}

p {
    margin-top: 25px;
    font-size: 1.2em;
}

img {
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    animation: fadeInUp 1s ease-out;
}

a {
    display: inline-block;
    margin-top: 30px;
    padding: 10px 20px;
    background-color: #00c853;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s ease;
}

a:hover {
    background-color: #00e676;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes zoomIn {
    0% { transform: scale(0.7); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}
```






