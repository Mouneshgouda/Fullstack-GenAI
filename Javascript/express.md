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

