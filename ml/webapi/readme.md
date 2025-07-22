
## Sapm detection

```python
from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np 
import joblib

app = Flask(__name__)

model = joblib.load('spam_model.pkl')

@app.route('/',methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    message = request.form.get('message')
    output = model.predict([message])
    if output == [0]:
      result = "This Message is Not a SPAM Message."
    else:
      result = "This Message is a SPAM Message." 
    return render_template('index.html', result=result,message=message) 
  else:
    return render_template('index.html')     


if __name__ == '__main__':
    app.run(debug=True)

```
#### index.html

```python


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPAM Detector</title>
</head>
<body>
    <h1>SPAM Detector</h1>

    <form action="/" method="post">
        <textarea name="message" rows="4" cols="50" placeholder="Enter a message"></textarea><br><br>
        <button type="submit">Check</button>
    </form>

    {% if message %}
        <h2>Message: {{ message }}</h2>
        <h3>{{ result }}</h3>
    {% endif %}
</body>
</html>


```

