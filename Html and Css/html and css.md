
# 🌐 HTML + 🎨 CSS Full Beginner Guide

A complete reference for HTML and CSS basics — structured, styled, and simplified.

---

## 🟠 HTML (HyperText Markup Language)

---

### 1. Basic Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

---

### 2. Common HTML Elements

#### Headings

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h6>Heading 6</h6>
```

#### Paragraphs & Line Breaks

```html
<p>This is a paragraph.</p>
<br />
```

#### Horizontal Rule

```html
<hr />
```

---

### 3. Text Formatting

```html
<b>Bold</b>
<strong>Strong</strong>
<i>Italic</i>
<em>Emphasized</em>
<u>Underline</u>
<mark>Highlighted</mark>
<small>Small text</small>
<del>Deleted</del>
<ins>Inserted</ins>
<sub>Subscript</sub>
<sup>Superscript</sup>
```

---

### 4. Links, Images & Media

```html
<a href="https://example.com" target="_blank">Go to Example</a>
<img src="image.jpg" alt="Description" width="200" />
<video controls width="320">
  <source src="movie.mp4" type="video/mp4">
</video>
<audio controls>
  <source src="sound.mp3" type="audio/mpeg">
</audio>
```

---

### 5. Lists

```html
<ul>
  <li>Unordered item</li>
</ul>

<ol>
  <li>Ordered item</li>
</ol>

<dl>
  <dt>HTML</dt>
  <dd>Markup Language</dd>
</dl>
```

---

### 6. Forms & Inputs

```html
<form action="/submit" method="post">
  <input type="text" placeholder="Your Name" required />
  <input type="email" />
  <input type="password" />
  <textarea></textarea>
  <select>
    <option>Option 1</option>
  </select>
  <input type="submit" />
</form>
```

---

### 7. Tables

```html
<table border="1">
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

### 8. Semantic Tags

```html
<header></header>
<nav></nav>
<main></main>
<article></article>
<section></section>
<aside></aside>
<footer></footer>
```

---

# HTML5 Semantic Tags Example

This is a simple example showing how to use semantic HTML5 elements like `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, and `<footer>`.

## Example Code

```html
<!DOCTYPE html>
<html>
<head>
  <title>Semantic Tags Example</title>
</head>
<body>

  <header>
    <h1>My Website</h1>
    <p>Welcome to my site!</p>
  </header>

  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">Blog</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <main>
    <article>
      <h2>Blog Post Title</h2>
      <p>This is the content of the blog post.</p>
    </article>

    <section>
      <h3>Related Articles</h3>
      <p>Links or summaries of related content can go here.</p>
    </section>
  </main>

  <aside>
    <h3>About Me</h3>
    <p>This is a short bio or sidebar content.</p>
  </aside>

  <footer>
    <p>&copy; 2025 My Website. All rights reserved.</p>
  </footer>

</body>
</html>
```
# HTML5 Semantic Elements

This document provides a brief description of key semantic HTML5 tags used for structuring web pages.

## Semantic Tags Overview

- **`<header>`**: Top section of the page, often for branding.
- **`<nav>`**: Navigation links.
- **`<main>`**: Main content of the document.
- **`<article>`**: Independent piece of content (e.g., blog post).
- **`<section>`**: Thematic grouping of content.
- **`<aside>`**: Side content, such as a sidebar or ads.
- **`<footer>`**: Bottom of the page, often with copyright.

  
## 🔵 CSS (Cascading Style Sheets)

---

### 1. Adding CSS

**Inline:**

```html
<h1 style="color: red;">Title</h1>
```

**Internal:**

```html
<style>
  h1 { color: blue; }
</style>
```

**External:**

```html
<link rel="stylesheet" href="style.css" />
```

---

### 2. CSS Syntax

```css
selector {
  property: value;
}
```

---

### 3. Selectors

```css
*         /* All elements */
p         /* Tag */
.box      /* Class */
#main     /* ID */
div p     /* Descendant */
h1, h2    /* Grouping */
```

---

### 4. Colors & Background

```css
color: red;
background-color: #eee;
background-image: url("bg.jpg");
```

---

### 5. Fonts & Text

```css
font-family: Arial;
font-size: 16px;
font-weight: bold;
text-align: center;
text-decoration: underline;
line-height: 1.5;
```

---

### 6. Box Model

```css
div {
  width: 100px;
  height: 100px;
  padding: 10px;
  margin: 20px;
  border: 2px solid black;
}
```

---

### 7. Positioning

```css
position: static | relative | absolute | fixed | sticky;
top: 10px;
left: 20px;
```

---

### 8. Flexbox

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

### 9. Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}
```

---

### 10. Pseudo-classes & Pseudo-elements

```css
a:hover {
  color: red;
}
p::first-line {
  font-weight: bold;
}
```

---

### 11. Media Queries

```css
@media (max-width: 600px) {
  body {
    background: lightgray;
  }
}
```

---

## ✅ Summary

- 🟠 HTML builds the structure  
- 🔵 CSS styles and layouts the page  
- 🧱 Core building blocks for web development

---

Happy Coding & Designing! 🎉
