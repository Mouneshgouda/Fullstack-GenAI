# 📝 Personal Diary & Mood Tracker

A web application where users can write daily diary entries and tag their mood. The app allows users to view, edit, delete entries and analyze mood trends over time.

---

## 📘 Project Description

This project is a lightweight personal diary and mood tracker built with Flask (Python), MongoDB (NoSQL database), and HTML/CSS using Jinja2 templates.

Users can:
- Log their daily thoughts
- Track moods like "happy", "anxious", "tired", etc.
- Analyze mood trends over time with charts
- Search entries by keywords, moods, or tags

---

## 🧠 Why This Project is Great

- **MongoDB** handles flexible diary entries with optional fields (mood, tags, etc.)
- **Flask** offers a simple and fast backend with easy routing
- **HTML + Jinja** for clean templating and dynamic content rendering

---

## 🔑 Key Features

### 📅 Diary System
- Create new entries with title, content, mood, and optional tags
- Edit, delete, or view past entries
- Store each entry with a timestamp in MongoDB

### 😊 Mood Tracker
- Choose from predefined moods (happy, sad, anxious, excited, etc.)
- Categorize entries by mood
- Visual mood calendar or mood frequency chart

### 🔍 Search & Filter
- Search by keyword, mood, date range, or tags

---

## 🛠️ Tech Stack

| Component     | Technology     |
|---------------|----------------|
| Backend       | Flask          |
| Database      | MongoDB (PyMongo) |
| Frontend      | HTML, CSS, Jinja2 |
| Visualization | Chart.js (optional) |

---

## 🧩 MongoDB Schema Example

```json
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "date": "2025-07-24",
  "title": "Rough Day at Work",
  "content": "Had a stressful meeting today...",
  "mood": "anxious",
  "tags": ["work", "stress"],
  "created_at": ISODate
}
```

## 🖼️ UI Pages
```python
Route	Page Description
/login	Login page for users
/register	Registration page
/dashboard	List of recent entries
/entry/new	Form to write a new entry
/entry/<id>	View/edit a specific entry
/mood-analytics	Mood frequency chart visualization

```
## 📂 Project Folder Structure

``` python
diary_mood_tracker/
├── app.py
├── requirements.txt
├── config.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── new_entry.html
│   ├── view_entry.html
│   └── mood_analytics.html
├── static/
│   ├── css/
│   └── js/
├── models/
│   └── user.py
│   └── entry.py
└── utils/
    └── auth.py

```

## app.py

```python

from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['diary_tracker']

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Registration logic here
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic here
    pass

@app.route('/dashboard')
def dashboard():
    # Show entries
    return render_template('dashboard.html')

@app.route('/entry/new', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'POST':
        entry = {
            "user": session['user'],
            "title": request.form['title'],
            "content": request.form['content'],
            "mood": request.form['mood'],
            "tags": request.form['tags'].split(','),
            "date": datetime.now()
        }
        db.entries.insert_one(entry)
        return redirect(url_for('dashboard'))
    return render_template('new_entry.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

## new_entry.html

```python

{% extends 'base.html' %}
{% block content %}
<h2>New Diary Entry</h2>
<form method="POST">
    <input type="text" name="title" placeholder="Title"><br>
    <textarea name="content" placeholder="What's on your mind?"></textarea><br>
    <label for="mood">Mood:</label>
    <select name="mood">
        <option>happy</option>
        <option>sad</option>
        <option>angry</option>
        <option>excited</option>
        <option>anxious</option>
    </select><br>
    <input type="text" name="tags" placeholder="Tags (comma separated)"><br>
    <button type="submit">Save Entry</button>
</form>
{% endblock %}

```
## Charts.js
```python
<canvas id="moodChart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('moodChart').getContext('2d');
  const moodChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Happy', 'Sad', 'Anxious', 'Excited'],
      datasets: [{
        label: '# of Moods',
        data: [5, 2, 4, 1],  // Replace with Jinja variable
        backgroundColor: ['#4CAF50', '#F44336', '#FF9800', '#2196F3']
      }]
    }
  });
</script>
```python



