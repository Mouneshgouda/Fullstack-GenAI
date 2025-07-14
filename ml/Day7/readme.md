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
```

