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



