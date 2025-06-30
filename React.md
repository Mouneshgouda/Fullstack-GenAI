
# Clint side Routing 

```python
You'll make these pages in src/pages/:

Home.jsx

About.jsx

Contact.jsx

```

### 🔹 1. src/pages/Home.jsx
```jsx

export default function Home() {
  return <h2>This is the Home Page</h2>;
}
```

###🔹 2. src/pages/About.jsx
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
##🔹 4. Update App.jsx
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
