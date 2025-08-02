

```python

import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from PIL import Image

# Load model
model = tf.keras.models.load_model('/content/modelnew.h5')

# Labels
labels = {
    0: 'cardboard',
    1: 'glass',
    2: 'metal',
    3: 'paper',
    4: 'plastic',
    5: 'trash'
}

# Prediction function
def predict_image(img):
    img = img.resize((300, 300))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    return {labels[i]: float(prediction[i]) for i in range(len(labels))}

# Example images (optional)
examples = [
    ["/content/Smart-Garbage-Segregation/Data/Test/cardboard/cardboard353.jpg"],
    ["/content/Smart-Garbage-Segregation/Data/Test/paper/paper522.jpg"],
    ["/content/Smart-Garbage-Segregation/Data/Test/metal/metal386.jpg"],
    ["/content/Smart-Garbage-Segregation/Data/Test/plastic/plastic430.jpg"]
]

# Using gr.Blocks for a better layout
with gr.Blocks(css=".gradio-container {background-color: #f8f9fa; font-family: 'Segoe UI';}") as demo:
    gr.Markdown("<h1 style='text-align: center; color: #2E86C1;'>🗑️ Smart Garbage Classifier</h1>")
    gr.Markdown("<p style='text-align: center;'>Upload or capture a trash image. The AI will predict if it's cardboard, plastic, glass, paper, metal, or trash.</p>")

    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="pil", label="📸 Upload Image")
            predict_btn = gr.Button("🔍 Classify")
        with gr.Column():
            output_label = gr.Label(num_top_classes=3, label="🧠 Prediction (Top 3 Classes)")

    predict_btn.click(fn=predict_image, inputs=input_img, outputs=output_label)

    gr.Examples(
        examples=examples,
        inputs=input_img,
        outputs=output_label,
        label="🎯 Try with Example Images"
    )

    gr.Markdown("<footer style='text-align: center; color: gray;'>Built with  using TensorFlow + Gradio</footer>")

demo.launch(debug=True)

```







