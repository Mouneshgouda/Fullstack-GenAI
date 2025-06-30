
# 🧠 JavaScript Basics + OOP Guide

A beginner-friendly summary of JavaScript essentials and object-oriented programming (OOP) — with short, simple code examples.

---

## 🟢 1. Variables

```js
let name = "John";  // changeable
const age = 25;     // fixed
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
if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

---

## 🟢 5. Loops

```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}

let n = 0;
while (n < 2) {
  console.log(n);
  n++;
}
```

---

## 🟢 6. Functions

```js
function greet(name) {
  return "Hi " + name;
}

const add = (a, b) => a + b;
```

---

## 🟢 7. Arrays

```js
let nums = [1, 2, 3];
nums.push(4);       // Add
nums.pop();         // Remove

let squares = nums.map(n => n * n); // [1, 4, 9]
```

---

## 🟢 8. Objects

```js
let user = {
  name: "Sara",
  age: 20,
  greet() {
    console.log("Hello!");
  }
};

console.log(user.name); // Sara
user.greet();
```

---

## 🟢 9. String Methods

```js
let text = "JavaScript";
console.log(text.length);          // 10
console.log(text.toUpperCase());  // "JAVASCRIPT"
console.log(text.includes("Script")); // true
```

---

## 🟢 10. Date & Math

```js
let today = new Date();
console.log(today.getFullYear());

console.log(Math.floor(4.9)); // 4
console.log(Math.random());   // 0 to 1
```

---

## 🟢 11. Error Handling

```js
try {
  throw new Error("Oops!");
} catch (e) {
  console.log(e.message);
}
```

---

## 🔵 Object-Oriented Programming (OOP)

---

### 🧱 1. Constructor Function

```js
function Person(name) {
  this.name = name;
  this.sayHi = () => console.log("Hi " + name);
}

let p = new Person("Ali");
p.sayHi();
```

---

### 🧱 2. Class (ES6)

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(this.name + " makes sound");
  }
}
let dog = new Animal("Dog");
dog.speak();
```

---

### 🧱 3. Inheritance

```js
class Dog extends Animal {
  speak() {
    console.log(this.name + " barks");
  }
}
let d = new Dog("Max");
d.speak(); // Max barks
```

---

### 🧱 4. Encapsulation (Private Field)

```js
class Bank {
  #balance = 0;
  deposit(amount) {
    this.#balance += amount;
  }
  getBalance() {
    return this.#balance;
  }
}
let acc = new Bank();
acc.deposit(100);
console.log(acc.getBalance()); // 100
```

---

## ✅ Summary

- 🔹 All key JavaScript basics  
- 🔹 Object-Oriented Programming (OOP) made simple  
- 🔹 Super short code examples  
- 🔹 Easy to understand and remember

---

Happy Coding! 🚀
