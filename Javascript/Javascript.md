
# 🧠 JavaScript Basics + OOP Guide

A beginner-friendly summary of JavaScript essentials and object-oriented programming (OOP) — with short, simple code examples.

---

## 🟢 1. Variables

```js
let name="mounesh";
const age=24;
console.log(age)
console.log(age)
```

---

## 🟢 2. Data Types

```js
let str = "hello";         // string  
let num = 123;             // number  
let isCool = true;         // boolean  
let arr = [1, 2, 3];       // array (object)  
let obj = {a: 1, b: 2};    // object  
let nothing = null;        // null (object)  
let unknown;               // undefined  

console.log(typeof str);       // "string"
console.log(typeof num);       // "number"
console.log(typeof isCool);    // "boolean"
console.log(typeof arr);       // "object"
console.log(typeof obj);       // "object"
console.log(typeof nothing);   // "object" (quirk in JS)
console.log(typeof unknown);   // "undefined"
  
```

---

## 🟢 3. Operators

```js

let sum=5+2

5==="5";

true &&false;
console.log(sum)
```

---

## 🟢 4. Conditions

```js
const age = 20; // Example value

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}

```

---

## 🟢 5. Loops

```js
// For loop: runs 3 times (i = 0, 1, 2)
for (let i = 0; i < 3; i++) {
  console.log(i);
}

// While loop: runs 2 times (n = 0, 1)
let n = 0;
while (n < 2) {
  console.log(n);
  n++;
}

```

---

## 🟢 6. Functions


```js
function add(a, b) {
  return a + b;
}

console.log(add(5, 3)); // Output: 8
```

```js
// Traditional function
function greet(name) {
  return "Hi " + name;
}

// Arrow function
const add = (a, b) => a + b;

// Example usage:
console.log(greet("Alice")); // Hi Alice
console.log(add(2, 3));      // 5

```

## 🍎 JavaScript Array Example

```javascript
## 🍇 JavaScript Array Operations


let fruits = ["Apple", "Banana", "Mango"];

console.log(fruits[0]); // Output: Apple
console.log(fruits[1]); // Output: Banana

fruits.push("Orange");      // Add at end
fruits.pop();               // Remove from end

console.log(fruits.length); // Get length of array

```

## 🧱 JavaScript Objects

### ✅ What is an Object?

An **object** stores data in key–value pairs.

---

### 🔹 Example:

```javascript
let person = {
  name: "Mounesh",
  age: 25,
  city: "Bangalore"
};

console.log(person.name);  // Output: Mounesh
console.log(person.age);   // Output: 25

#Add or Changes
person.age = 26;              // Update value
person.country = "India";     // Add new property
console.log(person);

```
## ⏱️ JavaScript Timing Events

JavaScript timing events let you run code after a delay or repeatedly at intervals.

---

### ✅ 1. `setTimeout()`
Runs code **once** after a specified time (in milliseconds).

```javascript
setTimeout(() => {
  console.log("Hello after 2 seconds");
}, 2000); // 2 seconds
```
## 🔁 JavaScript `setInterval()` Example

The `setInterval()` function runs code **repeatedly** at fixed time intervals.

```javascript
setInterval(() => {
  console.log("Repeating every 1 second");
}, 1000); // 1 second

```
## 🛑 Stopping JavaScript Timers

You can cancel `setTimeout()` and `setInterval()` using `clearTimeout()` and `clearInterval()`.

---

### 🔹 Example:

```javascript
// This timeout is set but immediately cleared, so it won't run
let timer = setTimeout(() => {
  console.log("This won't run");
}, 3000);

clearTimeout(timer); // Cancels the timeout

// This interval is set but immediately cleared, so it runs at most once
let repeater = setInterval(() => {
  console.log("Repeats");
}, 1000);

clearInterval(repeater); // Cancels the interval
```
## 🖱️ JavaScript DOM Events

DOM events allow JavaScript to react to user actions like clicks, typing, or hovering.

---

### ✅ 1. `onclick` – Click Event

```html
<button onclick="sayHello()">Click Me</button>

<script>
  function sayHello() {
    alert("Hello!");
  }
</script>
```
## ⌨️ JavaScript `onkeydown` Event Example

The `onkeydown` event triggers when a key is pressed in the input field.

```html
<input type="text" onkeydown="keyPressed()" />

<script>
  function keyPressed() {
    console.log("A key was pressed");
  }
</script>
```

## 📦 JSON (JavaScript Object Notation)

JSON is a lightweight data-interchange format, easy for humans to read and write, and easy for machines to parse and generate.

---

### 🔹 1. JSON Structure

- **Objects** use `{}` with key–value pairs:
  ```json
  {
    "name": "Mounesh",
    "age": 25,
    "skills": ["JavaScript", "HTML", "CSS"]
  }
```

## 🌐 Fetch API: Simple GET Request Example

The following example demonstrates how to use the Fetch API to retrieve JSON data from an endpoint, check for HTTP errors, and handle any network or parsing errors.


```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    // Check if the HTTP status indicates a successful response (status in the range 200–299)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parse the response body as JSON
    return response.json();
  })
  .then(data => {
    // `data` is now a JavaScript object converted from the JSON response
    console.log(data); // Logs the retrieved post object
  })
  .catch(error => {
    // Catches network errors or the Error thrown above
    console.error('Fetch error:', error);
  });
```


