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

