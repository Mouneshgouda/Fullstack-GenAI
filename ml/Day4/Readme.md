## Brain Tumor Dataset
```python
import os
import urllib
import zipfile

# Download and unzip the dataset
if not os.path.isfile('.zip'):
  urllib.request.urlretrieve("https://github.com/Mouneshgouda/Brain-Tumor-Data-Set/archive/refs/heads/main.zip", "cancer.zip")

zip_filename = "cancer.zip"
with zipfile.ZipFile("cancer.zip","r") as zip_ref:
    zip_ref.extractall(".")

```

## Dog-and-Cat-Dataset


```python

import os
import urllib
import zipfile

# Download and unzip the dataset
if not os.path.isfile('.zip'):
  urllib.request.urlretrieve("https://github.com/Mouneshgouda/Dog-and-Cat-Dataset/archive/refs/heads/main.zip", "Cat Dog Data Set.zip")

zip_filename = "Cat_Dog_Dataset.zip"
with zipfile.ZipFile("Cat Dog Data Set.zip","r") as zip_ref:
    zip_ref.extractall(".")

```
## plant disease

```python

import os
import urllib
import zipfile

# Download and unzip the dataset
if not os.path.isfile('plantdoc.zip'):
  urllib.request.urlretrieve("https://github.com/Mouneshgouda/PlantDoc-Dataset/archive/refs/heads/master.zip", "plantdoc.zip")

zip_filename = "plantdoc.zip"
with zipfile.ZipFile(zip_filename, "r") as zip_ref:
    zip_ref.extractall(".")
```

