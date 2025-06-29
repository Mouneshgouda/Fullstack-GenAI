
# 🌐 HTML + 🎨 CSS Basics Guide

A quick reference for learning HTML and CSS with clear, simple examples.

---

## 🟠 1. Basic HTML Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

---

## 🟠 2. HTML Headings & Paragraphs

```html
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<p>This is a paragraph.</p>
```

---

## 🟠 3. HTML Links & Images

```html
<a href="https://example.com">Visit Example</a>
<img src="image.jpg" alt="Description" />
```

---

## 🟠 4. HTML Lists

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<ol>
  <li>First</li>
  <li>Second</li>
</ol>
```

---

## 🟠 5. HTML Forms

```html
<form>
  <input type="text" placeholder="Name" />
  <input type="submit" value="Send" />
</form>
```

---

## 🟠 6. HTML Table

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Ali</td>
    <td>25</td>
  </tr>
</table>
```

---

## 🔵 1. Basic CSS Syntax

```css
selector {
  property: value;
}
```

---

## 🔵 2. Adding CSS to HTML

**Inline:**

```html
<p style="color: red;">Red Text</p>
```

**Internal:**

```html
<style>
  p { color: blue; }
</style>
```

**External:**

```html
<link rel="stylesheet" href="style.css" />
```

---

## 🔵 3. CSS Selectors

```css
/* Element selector */
p { color: green; }

/* Class selector */
.box { padding: 10px; }

/* ID selector */
#header { font-size: 20px; }
```

---

## 🔵 4. CSS Box Model

```css
div {
  margin: 10px;
  padding: 10px;
  border: 1px solid black;
}
```

---

## 🔵 5. CSS Flexbox

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

## 🔵 6. Responsive Design

```css
@media (max-width: 600px) {
  body {
    background: lightgray;
  }
}
```


---

## ✅ Summary

- 🟠 HTML: Structure of the web  
- 🔵 CSS: Styling and layout  
- 💡 Short examples, easy to remember  

Happy Designing! 🎨
