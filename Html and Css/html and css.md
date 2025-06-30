
# 🌐 HTML + 🎨 CSS Full Beginner Guide

A complete reference for HTML and CSS basics — structured, styled, and simplified.

---

## 🟠 HTML (HyperText Markup Language)

---
## 🔹 1. Basic Structure Tags in HTML

These are the foundational tags used to set up the structure of an HTML document.

| Tag            | Purpose                                 |
|----------------|-----------------------------------------|
| <!DOCTYPE html> | Declares the document type as HTML5. It ensures the browser renders the page in standards mode. |
| <html>       | Root element of the HTML document. It wraps all the content on the entire page. |
| <head>       | Contains meta-information about the document such as title, character encoding, linked stylesheets, etc. This content is *not* displayed on the webpage. |
| <title>      | Sets the title of the page. This title appears on the browser tab. |
| <body>       | Contains all the *visible content* of the webpage, such as headings, paragraphs, images, links, buttons, etc. |

### 📄 Example:
```
<!DOCTYPE html>
<html>
  <head>
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Welcome to my website</h1>
    <p>This is a basic HTML structure.</p>
  </body>
</html>
```

## 🔹 2. Headings & Paragraphs
```
This section includes tags used to define headings, paragraphs, and line breaks in HTML.

| Tag             | Purpose                                               |
|------------------|--------------------------------------------------------|
| <h1> to <h6> | Headings (<h1> is the largest, <h6> is the smallest) |
| <p>            | Paragraph of text                                     |
| <br>           | Line break                                            |
| <hr>           | Horizontal line (thematic break)                      |
```

## 🔹 3. Text Formatting Tags

| Tag         | Purpose                                               |
|--------------|--------------------------------------------------------|
| `<b>`        | Bold text (without importance)                        |
| `<strong>`   | Bold text (with importance)                           |
| `<i>`        | Italic text (without emphasis)                        |
| `<em>`       | Emphasized text (important italic)                    |
| `<u>`        | Underlined text                                       |
| `<mark>`     | Highlighted text                                      |
| `<sub>`      | Subscript (e.g., H<sub>2</sub>O)                       |
| `<sup>`      | Superscript (e.g., x<sup>2</sup>)                      |
| `<small>`    | Smaller text                                          |
| `<del>`      | Deleted text (strike-through)                         |
| `<ins>`      | Inserted text (usually underlined)                    |

---

## 🔹 4. Links and Media

| Tag         | Purpose                                                |
|--------------|--------------------------------------------------------|
| `<a>`        | Anchor tag for hyperlinks (`href`)                    |
| `<img>`      | Embeds an image (`src`, `alt`)                        |
| `<audio>`    | Embeds audio (`controls`, `src`)                      |
| `<video>`    | Embeds video (`controls`, `src`, `poster`)           |
| `<source>`   | Specifies multiple media sources                      |
| `<iframe>`   | Embeds another webpage or content                     |

---

## 🔹 5. Lists

| Tag         | Purpose                                                |
|--------------|--------------------------------------------------------|
| `<ul>`       | Unordered list (bullets)                              |
| `<ol>`       | Ordered list (numbers)                                |
| `<li>`       | List item                                              |
| `<dl>`       | Description list                                      |
| `<dt>`       | Term in a description list                            |
| `<dd>`       | Description of the term                               |

---

## 🔹 6. Tables

| Tag         | Purpose                                                |
|--------------|--------------------------------------------------------|
| `<table>`    | Starts a table                                        |
| `<tr>`       | Table row                                             |
| `<td>`       | Table data (cell)                                     |
| `<th>`       | Table header cell                                     |
| `<thead>`    | Header section of a table                             |
| `<tbody>`    | Body section of a table                               |
| `<tfoot>`    | Footer section of a table                             |
| `colspan`    | Span multiple columns                                 |
| `rowspan`    | Span multiple rows                                    |

---

## 🔹 7. Forms and Input

| Tag           | Purpose                                                |
|----------------|--------------------------------------------------------|
| `<form>`        | Defines a form                                        |
| `<input>`       | Input field (text, password, email, checkbox, etc.) |
| `<label>`       | Label for input fields                               |
| `<textarea>`    | Multi-line input box                                 |
| `<select>`      | Dropdown menu                                        |
| `<option>`      | Option inside `<select>`                             |
| `<button>`      | Clickable button                                     |
| `<fieldset>`    | Group related fields in a form                       |
| `<legend>`      | Title for `<fieldset>`                               |

---

## 🔹 8. Semantic HTML5 Tags

| Tag           | Purpose                                                |
|----------------|--------------------------------------------------------|
| `<header>`      | Top section of a webpage (logo, nav, etc.)           |
| `<footer>`      | Bottom section (copyright, links)                    |
| `<main>`        | Main content area                                    |
| `<section>`     | Logical section of the content                       |
| `<article>`     | Independent content unit (e.g., blog post)           |
| `<aside>`       | Sidebar or related content                           |
| `<nav>`         | Navigation links                                     |
| `<figure>`      | Image with a caption                                 |
| `<figcaption>`  | Caption for the image or media inside `<figure>`    |

---

## 🔹 9. Meta & Miscellaneous

| Tag           | Purpose                                                |
|----------------|--------------------------------------------------------|
| `<meta>`        | Defines metadata like charset, description, etc.     |
| `<link>`        | Links to external resources (CSS, favicon)           |
| `<script>`      | Embeds or links JavaScript                           |
| `<style>`       | Embeds CSS directly into HTML                        |
| `<noscript>`    | Content to show if JS is disabled                    |


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


# CSS - Complete Guide

## 🌐 What is CSS?

CSS (Cascading Style Sheets) is used to style and design HTML elements. It controls the layout, colors, fonts, spacing, and responsiveness of a webpage.

## 🎯 Purpose of CSS

* To separate content from design
* To style HTML elements
* To make web pages visually appealing
* To build responsive and mobile-friendly designs
* To enable reusability and maintainability

---

## 🔹 1. CSS Syntax

```
selector {
  property: value;
}
```

Example:

```css
h1 {
  color: blue;
  font-size: 24px;
}
```

---

## 🔹 2. Types of CSS

| Type         | Description                                 |
| ------------ | ------------------------------------------- |
| Inline CSS   | Inside HTML element using `style` attribute |
| Internal CSS | Inside `<style>` tag in the `<head>`        |
| External CSS | Linked using `<link href="style.css">`      |

---

## 🔹 3. CSS Selectors

| Selector             | Description                               |
| -------------------- | ----------------------------------------- |
| `*`                  | Universal selector (selects all elements) |
| `p`                  | Element selector                          |
| `.class`             | Class selector                            |
| `#id`                | ID selector                               |
| `element1, element2` | Group selector                            |
| `element element`    | Descendant selector                       |
| `element > element`  | Child selector                            |
| `element + element`  | Adjacent sibling selector                 |
| `element ~ element`  | General sibling selector                  |

---

## 🔹 4. Common CSS Properties

| Property           | Description                       |
| ------------------ | --------------------------------- |
| `color`            | Text color                        |
| `background-color` | Background color                  |
| `font-size`        | Size of text                      |
| `font-family`      | Font type                         |
| `text-align`       | Align text                        |
| `margin`           | Space outside element             |
| `padding`          | Space inside element              |
| `border`           | Border around element             |
| `width`/`height`   | Set dimensions                    |
| `display`          | Block, inline, flex, grid, etc.   |
| `position`         | static, relative, absolute, fixed |
| `top`/`left`/etc.  | Position offsets                  |
| `z-index`          | Stack order                       |
| `overflow`         | What to do when content overflows |

---

## 🔹 5. Box Model

* **Content** → **Padding** → **Border** → **Margin**
* Understanding box model helps in spacing, layout, and alignment.

---

## 🔹 6. Colors & Units

| Type   | Example Values                     |
| ------ | ---------------------------------- |
| Color  | `red`, `#ff0000`, `rgb(255,0,0)`   |
| Length | `px`, `em`, `rem`, `%`, `vh`, `vw` |

---

## 🔹 7. Pseudo-Classes & Elements

| Pseudo     | Description                   |
| ---------- | ----------------------------- |
| `:hover`   | When mouse hovers             |
| `:active`  | When clicked                  |
| `:focus`   | When input is focused         |
| `::before` | Insert content before element |
| `::after`  | Insert content after element  |

---

## 🔹 8. Flexbox (Layout)

| Property          | Description              |
| ----------------- | ------------------------ |
| `display: flex`   | Enables flex container   |
| `flex-direction`  | row / column             |
| `justify-content` | Align items horizontally |
| `align-items`     | Align items vertically   |
| `gap`             | Space between items      |

---

## 🔹 9. Grid (Advanced Layout)

| Property                  | Description                |
| ------------------------- | -------------------------- |
| `display: grid`           | Enables grid layout        |
| `grid-template-columns`   | Define column layout       |
| `grid-template-rows`      | Define row layout          |
| `gap`                     | Space between rows/columns |
| `grid-column`, `grid-row` | Span over rows/columns     |

---

## 🔹 10. Responsive Design

| Technique       | Description                             |
| --------------- | --------------------------------------- |
| Media Queries   | Apply styles for different screen sizes |
| `%`, `vh`, `vw` | Use flexible units                      |
| `flex`, `grid`  | Responsive layout systems               |
| `max-width`     | Prevent overflow                        |

Example:

```css
@media screen and (max-width: 768px) {
  body {
    font-size: 14px;
  }
}
```

---

## 🔹 11. Animation & Transition

| Property     | Description                 |
| ------------ | --------------------------- |
| `transition` | Smooth change of properties |
| `animation`  | Keyframe-based animation    |
| `@keyframes` | Define animation steps      |

Example:

```css
div {
  transition: background 0.5s ease;
}

@keyframes slideIn {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}
```

---


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
