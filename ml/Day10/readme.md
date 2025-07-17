### app.py
```python --

import os
print("my first image")
print("current Dir is:",os.getcwd())

```
### Dockerfile
```python 
FROM python
WORKDIR /app
COPY . /app
CMD [ "python3","app.py" ]
```

### cmd
```python
docker build -t myfirstp
ythonapp .

docker run myfirstpythonapp

docker run --name  myfir
st  myfirstpythonapp
```

