
# 🧠 JavaScript Basics + OOP Guide

A beginner-friendly summary of JavaScript essentials and object-oriented programming (OOP) — with short, simple code examples.

---

## 🟢 1. Variables

```js
let name="mounesh";
const age=25;
console.log(age)
console.log(age)
```

---

## 🟢 2. Data Types

```js
let str = "hello";         // string  
let num = 123;             // number  
let isCool = true;         // boolean  
let arr = [1, 2, 3];       // array  
let obj = {a: 1, b: 2};    // object  
let nothing = null;        // null  
let unknown;               // undefined  
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


