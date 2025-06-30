### 1. Editing App.jsx

- Inside your project folder:

- Go to src/App.jsx

- You’ll see something like this:

```jsx

function App() {
  return (
    <div>
      <h1>Vite + React</h1>
      <p>Click on the Vite and React logos to learn more</p>
    </div>
  );
}

export default App;
```
Try changing the <h1> text:

``jsx

<h1>Hello, Mounesh!</h1>
```
- Save the file — your browser updates instantly. That’s called hot reload.

### 🔹 2. Creating Your First Component
- A component is just a function that returns JSX.

- 👉 Inside src, make a new file: Welcome.jsx

```jsx

function Welcome() {
  return <h2>Welcome to your first React app!</h2>;
}

export default Welcome;
```
Now update App.jsx to use it:

```jsx

import Welcome from './Welcome';

function App() {
  return (
    <div>
      <h1>Hello, Mounesh!</h1>
      <Welcome />
    </div>
  );
}

export default App;
```
Now you’ll see both headings in your browser.

### 🔹 3. Basic File Structure
- Here’s what each important file/folder does:

```css

mounesh/
├── index.html            ← The single HTML file
├── package.json          ← Project info and dependencies
├── vite.config.js        ← Vite settings
└── src/
    ├── main.jsx          ← App entry point (renders App.jsx)
    ├── App.jsx           ← Your main component
    └── Welcome.jsx       ← (You created this!)
```

### ✅ Simple Counter with useState
- Create a new component Counter.jsx inside the src/components/ folder:

```jsx

import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0); // count = current value, setCount = function to update it

  return (
    <div>
      <h3>Counter: {count}</h3>
      <button onClick={() => setCount(count + 1)}>+ Increment</button>
      <button onClick={() => setCount(count - 1)}>- Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

export default Counter;

```

### 🧩 Use It in App.jsx
```jsx

import Counter from './components/Counter';

function App() {
  return (
    <div>
      <h1>Simple Hook Example</h1>
      <Counter />
    </div>
  );
}

export default App;

```

## File Structure
```python
mounesh/                ← Your project folder
├── public/             ← Static files (like favicon, images)
├── src/                ← Your app source code
│   ├── components/     ← Reusable UI parts (e.g., Header, Navbar)
│   ├── pages/          ← Full-page components (e.g., Home, About)
│   ├── App.jsx         ← Main app logic, includes routing
│   ├── main.jsx        ← Entry point, renders <App />
│   ├── App.css         ← Optional: global styles
│   └── index.css       ← Optional: reset styles or base styles
├── package.json        ← Lists dependencies (like react-router-dom)
└── vite.config.js      ← Vite configuration
```



# Clint side Routing 

```python
You'll make these pages in src/pages/:

Home.jsx

About.jsx

Contact.jsx

```
```python
npm install react-router-dom

```

### 🔹 1. src/pages/Home.jsx
```jsx

export default function Home() {
  return <h2>This is the Home Page</h2>;
}
```

### 🔹 2. src/pages/About.jsx
```jsx

export default function About() {
  return <h2>This is the About Page</h2>;
}
```
### 🔹 3. src/pages/Contact.jsx
```jsx

export default function Contact() {
  return <h2>This is the Contact Page</h2>;
}
```
### 🔹 4. Update App.jsx
- Now define the routes and navigation bar in App.jsx:

```jsx

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {
  return (
    <BrowserRouter>
      <nav style={{ marginBottom: '20px' }}>
        <Link to="/">Home</Link> |{" "}
        <Link to="/about">About</Link> |{" "}
        <Link to="/contact">Contact</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### ✅ Final Result
- You can now click Home, About, or Contact.

- The page updates without a reload.

- This is full client-side routing using React Router.
