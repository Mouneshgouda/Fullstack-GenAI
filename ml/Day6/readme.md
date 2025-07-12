```python
import torch
from PIL import Image
from torchvision.transforms.functional import to_tensor,to_pil_image
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2", device=device)
model.eval()
def to_animegan2(input_file):
  input_image = Image.open(input_file).convert('RGB')
  input_tensor = to_tensor(input_image).unsqueeze(0) * 2 - 1
  output = model(input_tensor.to(device)).cpu()[0]
  output = (output * 0.5 + 0.5).clip(0, 1)
  return to_pil_image(output)

```

```python

pil_image=to_animegan2('/content/face.jpg')
display(pil_image)
```

```python
model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="celeba_distill", device=device).eval()
display(to_animegan2('/content/face.jpg'))
```


## API KEY
```python

import getpass 
import os
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter-Your-GOOGLE_API_KEY")
```

### Text to Img

```python


import base64
from IPython.display import Image,display
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-preview-image-generation")


message = {
    "role": "user",
    "content": "Dog with hat,sunglass",
}
response = llm.invoke(
    [message],
    generation_config=dict(response_modalities=["TEXT", "IMAGE"]),
)

def _get_image_base64(response: AIMessage) -> None:
    image_block = next(
        block
        for block in response.content
        if isinstance(block, dict) and block.get("image_url")
    )
    return image_block["image_url"].get("url").split(",")[-1]

image_base64 = _get_image_base64(response)
display(Image(data=base64.b64decode(image_base64), width=400))

```

# UI Interface
```python
import base64
from io import BytesIO
from PIL import Image as PILImage
import gradio as gr

from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-preview-image-generation")

# Image generation function
def generate_image(prompt):
    try:
        message = {
            "role": "user",
            "content": prompt,
        }

        response = llm.invoke(
            [message],
            generation_config=dict(response_modalities=["TEXT", "IMAGE"])
        )

        for block in response.content:
            if isinstance(block, dict) and block.get("image_url"):
                image_url = block["image_url"].get("url")
                image_base64 = image_url.split(",")[-1]
                image_bytes = base64.b64decode(image_base64)
                image = PILImage.open(BytesIO(image_bytes))
                return image

        return "No image found in the response. Try a more descriptive prompt."
    except Exception as e:
        return f"Error: {e}"

# Create UI
gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your image prompt"),
    outputs="image",
    title="Gemini 2.0 Flash Image Generator",
    description="Type a prompt (e.g., 'a girl near a lake at sunset, DSLR style') and see what Gemini generates!",
    theme="default"
).launch()
```

# translater
```python

import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter-Your-GOOGLE_API_KEY")
```


```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
   
)
```

```python
def get_translate(user_text,):
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to . Translate the user sentence.",
        ),
        ("human", user_text),
    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content


```


```python
def get_translation(user_text, target_language):
    messages = [
        (
            "system",
            f"You are a helpful assistant that translates English to {target_language}. Translate the user sentence clearly and accurately.",
        ),
        ("human", user_text),
    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content
```

```python

print(get_translation("How are you?", "telugu"))

```

# DEEFAKE

```python
!sudo apt install nvidia-cudnn -y --yes --fix-missing

```
```python
!git clone https://github.com/neuromodern/VideoFake.git
```
```python

!pip install onnxruntime-gpu --upgrade

```

```python
!pip install customtkinter
```

```python

pip install tkinterdnd2

```

```python
!pip install -U insightface
````
# git Clone
```python
import shutil
import os

directory = "/content/VideoFake/roop/models/"

# Create the directory if it doesn't already exist
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' created successfully!")
else:
    print(f"Directory '{directory}' already exists!")
```

# Deefake

```python

source = "/content/VideoFake/face.jpg"
target = "/content/VideoFake/input_video.mp4"
output = "/content/VideoFake/out.mp4"

Device = "cuda"
Processor = "face_swapper"  # ✅ Safe single value
VideoEncoder = "libx264"
VideoQuality = "18"

KeepFPS = True
KeepAudio = True
KeepFrames = False
ManyFaces = True

KeepFPS_flag = "--keep-fps" if KeepFPS else ""
KeepAudio_flag = "" if KeepAudio else "--skip-audio"
KeepFrames_flag = "--keep-frames" if KeepFrames else ""
ManyFaces_flag = "--many-faces" if ManyFaces else ""

cmd = f"""
python /content/VideoFake/roop/run.py \
--execution-provider {Device} \
--source {source} \
-t {target} \
-o {output} \
--frame-processor {Processor} \
--output-video-encode {VideoEncoder} \
--output-video-quality {VideoQuality} \
{KeepFPS_flag} {KeepAudio_flag} {KeepFrames_flag} {ManyFaces_flag}
"""

print("Running command:")
print(cmd)
!{cmd}
```










