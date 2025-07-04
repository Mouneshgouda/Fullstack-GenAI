# 🧱 Express.js Basic Setup Guide

## 1. Setup and Installation

To start using Express:

```bash
npm init -y              # Initialize a Node.js project
npm install express      # Install Express.js
```
## 2. Import and Create App

```javascript
const express = require('express');
const app = express();
```

## 3. Define Routes

Routes define how your app responds to different HTTP requests:

```javascript
app.get('/', (req, res) => {
  res.send('Hello, World!');
});
```

## 4. Start the Server

```javascript
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```

## 5. Middleware

Middleware functions run before your route handlers.

They can be used to process requests, handle logging, authentication, etc.

Example: to parse JSON data from incoming requests:

```javascript
app.use(express.json()); // Now you can access JSON data via req.body
```

## 6. Serve Static Files

To serve static files like HTML, CSS, or images:

```javascript
app.use(express.static('public')); // 'public' is the folder name
```
## 7. Basic Folder Structure
```
project/
├── public/ # Static files (HTML, CSS, JS)
│ └── index.html
├── routes/ # (Optional) Route modules
├── index.js # Main server file
└── package.json # Project metadata and dependencies
```





## Express


```js
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
const port = 3000;

// Setup __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Handle form POST
app.post('/submit', (req, res) => {
  const { name, email } = req.body;
  res.send(`<h2>Thanks, ${name} (${email})! Your form was submitted.</h2>`);
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/form.html`);
});
```

## 
```js

<!DOCTYPE html>
<html>
<head>
  <title>Simple Form</title>
</head>
<body>
  <h2>User Form</h2>
  <form action="/submit" method="POST">
    <label>Name:</label><br>
    <input type="text" name="name" required><br><br>

    <label>Email:</label><br>
    <input type="email" name="email" required><br><br>

    <button type="submit">Submit</button>
  </form>
</body>
</html>
```
# Mail share
## form.html
```js
<!DOCTYPE html>
<html>
<head>
  <title>Simple Form</title>
</head>
<body>
  <h2>User Form</h2>
  <form action="/submit" method="POST">
    <label>Name:</label><br>
    <input type="text" name="name" required><br><br>

    <label>Email:</label><br>
    <input type="email" name="email" required><br><br>

    <button type="submit">Submit</button>
  </form>
</body>
</html>

```

## Express.js
```js
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();
const port = 3000;

// Setup __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Handle form POST
app.post('/submit', (req, res) => {
  const { name, email } = req.body;
  res.send(`<h2>Thanks, ${name} (${email})! Your form was submitted.</h2>`);
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/form.html`);
});


```

### First Api Server running
```

// app.js
import express from 'express';

const app = express();
const PORT = 3000;

app.get('', (req, res) => {
res.send('Hello GURANNA! Welcome to your first API 🎉');
});

app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
```

## Api Routing 
```
import express from 'express';
const app = express();
const PORT = 3000;

// Home route
app.get('/', (req, res) => {
  res.send('Welcome to Home Page');
});

// About route
app.get('/about', (req, res) => {
  res.send('This is the About Page');
});

// Contact route
app.get('/contact', (req, res) => {
  res.send('Contact us at example@example.com');
});

// Dynamic route with parameter
app.get('/user/:username', (req, res) => {
  const name = req.params.username;
  res.send(`Hello, ${name}!`);
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
```



# Sending Info To Server
```
// app.js
import express from 'express';

const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/submit', (req, res) => {
  const { name, email } = req.body;
  res.send(`Received data for ${name} with email: ${email}`);
});

app.listen(PORT, () => {
  console.log(`Server live at http://localhost:${PORT}`);
});
```
