

```python

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from PIL import Image

model = load_model('pneumonia_model.h5')  # Upload your pneumonia model here

IMG_SIZE = 64 

uploaded = files.upload()

for file_name in uploaded.keys():
    img_path = file_name
    img = Image.open(img_path).resize((IMG_SIZE, IMG_SIZE))

    if img.mode != 'RGB':
        img = img.convert('RGB')

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]
    label = "PNEUMONIA" if prediction > 0.5 else "Normal"
    confidence = prediction if prediction > 0.5 else 1 - prediction

    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Prediction: {label} ({confidence:.2%} confidence)")
    plt.show()
```

## gradio UI

```python
import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("pneumonia_model.h5")
IMG_SIZE = 64
class_names = ['Normal', 'Pneumonia']

def predict(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))  
    image_array = np.array(image) / 255.0      
    image_array = image_array.reshape(1, IMG_SIZE, IMG_SIZE, 3)  
    prediction = model.predict(image_array)[0][0]
    label = class_names[1] if prediction >= 0.5 else class_names[0]
    confidence = prediction if prediction >= 0.5 else 1 - prediction
    return f"{label} ({confidence*100:.2f}% confidence)"
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Text(label="Prediction"),
    title="Pneumonia Detector",
    description="Upload a chest X-ray pneumonia."
)
interface.launch()
```


## Streamlit pneumonia

```python

import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


@st.cache(allow_output_mutation=True)
def get_model():
    return load_model('pneumonia_model.h5')

model = get_model()

IMG_DIM = 64  
st.header("Chest X-ray Pneumonia Classifier")

uploaded_img = st.file_uploader("Choose an X-ray image file", type=['png', 'jpg', 'jpeg'])

if uploaded_img:

    img = Image.open(uploaded_img).convert('RGB').resize((IMG_DIM, IMG_DIM))


    st.image(img, caption='Uploaded X-ray', use_column_width=True)


    img_data = np.asarray(img) / 255.0
    img_data = img_data[np.newaxis, ...]


    pred_prob = model.predict(img_data)[0][0]


    if pred_prob > 0.5:
        diagnosis = "PNEUMONIA"
        confidence = pred_prob
    else:
        diagnosis = "Normal"
        confidence = 1 - pred_prob

    st.markdown(f"### Prediction: **{diagnosis}**")
    st.markdown(f"### Confidence: **{confidence:.2%}**")
```
