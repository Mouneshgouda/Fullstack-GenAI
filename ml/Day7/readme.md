## Image 

```python
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image #image Process
import torch

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img=Image.open("/content/Cat_November_2010-1a.jpg").convert("RGB")

input=processor(images=img,return_tensors="pt")

out=model.generate(**input)
caption=processor.decode(out[0],skip_special_tokens=True)
print("caption",caption)
```
## Q and A

```python

from transformers import ViltProcessor,ViltForQuestionAnswering
import requests
from PIL import Image

processor=ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model=ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

image = Image.open("/content/Cat_November_2010-1a.jpg")
text = "cat  color" #q
image

input=processor(image,text,return_tensors="pt")

import torch
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

outputs = model(**input)
logits = outputs.logits
idx = torch.sigmoid(logits).argmax(-1).item()
print("Predicted answer:", model.config.id2label[idx])

```
## Image to REcipe

```python


import gradio as gr
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


recipe_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
recipe_model = GPT2LMHeadModel.from_pretrained("gpt2")

def image_to_recipe(image):
    image = image.convert("RGB")
    inputs = caption_processor(images=image, return_tensors="pt")
    caption_ids = caption_model.generate(**inputs)
    caption = caption_processor.decode(caption_ids[0], skip_special_tokens=True)

    
    prompt = f"Write a detailed recipe for: {caption}\n\nIngredients:\n"
    inputs = recipe_tokenizer(prompt, return_tensors="pt")
    output = recipe_model.generate(**inputs, max_length=250, do_sample=True, temperature=0.9)
    recipe = recipe_tokenizer.decode(output[0], skip_special_tokens=True)

    return f"**Caption:** {caption}\n\n **Recipe:**\n{recipe}"

gr.Interface(
    fn=image_to_recipe,
    inputs=gr.Image(type="pil", label="Upload Food Image"),
    outputs=gr.Markdown(),
    title="AI Image to Recipe Generator",
    description="Upload a food image, and the AI will generate a caption + Recipe"
).launch()
```
## Img(mood) To Song 

```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import random
from google.colab import files
from IPython.display import display, HTML

# STEP 3: Define moods and songs
moods = ["happy", "sad", "chill", "dark", "energetic", "lonely", "calm"]

famous_songs = {
    "happy": [("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs")],
    "sad": [("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA")],
    "chill": [("Sunflower - Post Malone", "https://www.youtube.com/watch?v=ApXoWvfEYVU")],
    "dark": [("Lose Yourself - Eminem", "https://www.youtube.com/watch?v=_Yhyp-_hX2s")],
    "energetic": [("Believer - Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc")],
    "lonely": [("See You Again - Wiz Khalifa", "https://www.youtube.com/watch?v=RgKAFK5djSk")],
    "calm": [("Fix You - Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM")]
}

# STEP 4: Load CLIP model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# STEP 5: Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
image = Image.open(image_path).convert("RGB")
```




