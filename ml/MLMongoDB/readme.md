## LOGIN AND REGISTER

### register
```python
<h2>Register</h2>
<form method="POST">
  <input name="username" placeholder="Username" required><br>
  <input name="password" type="password" placeholder="Password" required><br>
  <button type="submit">Register</button>
</form>

<p>Already have an account?
  <a href="{{ url_for('login') }}">Go to Login</a>
</p>
```
### LOGiN

```python

<h2>Login</h2>
<form method="POST">
  <input name="username" placeholder="Username" required><br>
  <input name="password" type="password" placeholder="Password" required><br>
  <button type="submit">Login</button>
</form>

<p>Don't have an account?
  <a href="{{ url_for('register') }}">Go to Register</a>
</p>
```

### HOME

```python

<h2>Welcome {{ username }}!</h2>
<p>You are now on the home page.</p>
<a href="{{ url_for('logout') }}">Logout</a>
```

### app.py

```python

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.simpledb
users = db.users

# Not secure – used here only for simple demo logic
current_user = None

# Redirect root URL to register page
@app.route('/')
def index():
    return redirect(url_for('register'))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.find_one({'username': username}):
            return "User already exists!"

        users.insert_one({'username': username, 'password': password})
        return "Registered successfully!"

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.find_one({'username': username, 'password': password})
        if user:
            current_user = username
            return redirect(url_for('home'))
        else:
            return "Invalid username or password"

    return render_template('login.html')

# Home page (after login)
@app.route('/home')
def home():
    if current_user:
        return render_template('home.html', username=current_user)
    return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    global current_user
    current_user = None
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)




```


















