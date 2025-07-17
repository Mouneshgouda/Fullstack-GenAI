
```python --app.py

import os
print("my first image")
print("current Dir is:",os.getcwd())

```
```python Dockerfile
FROM python
WORKDIR /app
COPY . /app
CMD [ "python3","app.py" ]
```
