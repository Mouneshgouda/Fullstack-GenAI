# 🛠️ Build Your Own IoT Device Management API (with Flask)

This hands-on guide will help you write a complete Flask-based API from scratch. Each step contains **instructions**, **hints**, and **clues** to help you understand what you’re doing and why.

---

## 🧩 Step 1: Import Required Modules

🔍 **Goal:** Start by importing the tools you'll need to build a web server and handle API requests.

🧠 **Clues:**
- You'll need to create a Flask app.
- You want to accept JSON from clients and return JSON responses.

✅ **What to include:**
- The `Flask` class itself.
- `request` to read incoming request data.
- `jsonify` to return dictionary data as JSON.

```python
# Import the main class from the Flask module
# Import the request and jsonify utilities
```
## 🧩 Step 2: Create the Flask Application

🔍 **Goal:** Initialize your Flask application.

🧠 **Clues:**
- Use the `Flask` class from the module you imported.
- Pass the special variable `__name__` as an argument.
- This tells Flask where to find your code and resources.

✍️ **Your Task:**
Write a line of code that creates your Flask app instance.

💡 **Hint:** The object you create here will be used to define all your API routes.

```python
# Initialize the app using Flask(__name__)
```


## 🧩 Step 4: Create Route to Get All Devices

🔍 **Goal:** Make a `GET` request that returns the full device list.

🧠 **Clues:**
- Use the `@app.route()` decorator to define the endpoint.
- The route should be `/devices`.
- Set the `methods` parameter to `['GET']`.
- Return the entire `devices` dictionary using `jsonify()`.

✍️ **Your Task:**  
Define a function that handles this route and returns all devices.

💡 **Hint:** Flask matches the route and calls your function.

```python
# Define a GET route that returns all devices
```
## 🧩 Step 5: Create Route to Get a Specific Device

🔍 **Goal:** Allow clients to request a single device by name.

🧠 **Clues:**
- The route path should look like `/devices/<name>`.
- Use the `GET` method.
- Check if the device exists in your `devices` dictionary.
- If found, return its details using `jsonify()`.
- If not found, return a JSON error message and a 404 status code.

✍️ **Your Task:**
Write a route handler to return one specific device's information.

```python
# Define a GET route that accepts a device name and returns it
```

## 🧩 Step 6: Create Route to Add a New Device

🔍 **Goal:** Accept a new device from the client and add it to your dictionary.

🧠 **Clues:**

- This should be a `POST` route at `/devices`.
- Use `request.get_json()` to read the request body.
- Extract the following from the received JSON:
  - `"name"` of the device (e.g., `"AC"`)
  - `"status"` (e.g., `"on"` or `"off"`)
  - `"energy_kWh"` (a number)
- Check if the device name **already exists** in the dictionary.
  - ✅ If it **does not exist**, add it and return the device with HTTP status `201 Created`.
  - ❌ If it **already exists**, return an error with HTTP status `400 Bad Request`.

✍️ **Your Task:**  
Write a `POST` route that:
- Reads input from the request body
- Validates the input
- Adds the new device to your `devices` dictionary

💡 **Hint:** Use an `if` condition to check if the name is already in the dictionary before inserting.

```python
# Define a POST route to add a device
```

## 🧩 Step 7: Create Route to Update a Device

🔍 **Goal:** Modify the status or energy usage of an existing device.

🧠 **Clues:**

- This should be a `PUT` route with the URL pattern `/devices/<name>`.
- Use the `name` parameter from the URL to identify the device.
- Before updating, check if the device exists in the `devices` dictionary:
  - ❌ If it **does not exist**, return a JSON error message with HTTP status `404`.
  - ✅ If it **does exist**, use the `.update()` method with the data sent by the client to modify its values.

- The update can change one or both of the fields:
  - `"status"`
  - `"energy_kWh"`

✍️ **Your Task:**
Create a route to update a device's status or energy usage using data provided in the request body.

💡 **Hint:**
- Use `request.get_json()` to read the data.
- Use the dictionary’s `.update()` method to apply the changes.

```python
# Define a PUT route to update an existing device
```

## 🧩 Step 8: Create Route to Delete a Device

🔍 **Goal:** Allow the client to delete a device by its name.

🧠 **Clues:**

- This should be a `DELETE` route at `/devices/<name>`.
- Use the `name` from the URL to check if the device exists in the `devices` dictionary.

- ❌ If the device **does not exist**, return:
  - A JSON error message (e.g., `"Device not found"`)
  - HTTP status code `404 Not Found`

- ✅ If the device **does exist**:
  - Remove it using the Python `del` keyword.
  - Return a success message like: `"Device deleted"` or `"Fan deleted"`.

✍️ **Your Task:**
Create a route that deletes a device from your in-memory dictionary and responds appropriately.

💡 **Hint:**
- Use `del devices[name]` to remove the key.
- Respond using `jsonify()` for consistent output format.

```python
# Define a DELETE route to remove a device
```
## 🧩 Step 9: Run Your Flask App

🔍 **Goal:** Make sure your app only runs when this file is executed directly (not when imported into another Python script).

🧠 **Clues:**

- Use Python’s special conditional:  
  `if __name__ == '__main__':`
- Inside that block, call:  
  `app.run(debug=True)`
- `debug=True` helps during development by showing helpful error messages and auto-restarting the server when you make changes.

✍️ **Your Task:**
Write a conditional block that starts the Flask development server.

💡 **Hint:** Make sure this is placed at the bottom of your script.

```python
# Start the Flask app using app.run()

```
## 🧪 Testing Ideas

Once you've completed all your API routes, it's time to test your code!

You can use the following tools to interact with your Flask API:

### 🔧 Tools to Test Your API:
- **Postman** – A user-friendly GUI tool for sending HTTP requests.
- **curl** – Command-line tool to send requests and see responses.
- **JavaScript fetch()** – Run API requests directly from the browser console or a frontend app.

---

### 📌 Try These Test Cases:

✅ **Add a new device** using a `POST` request to `/devices`.  
✅ **Get all devices** using a `GET` request to `/devices`.  
✅ **Get a specific device** using a `GET` request to `/devices/Light`.  
✅ **Update an existing device** using a `PUT` request to `/devices/Light`.  
✅ **Delete a device** using a `DELETE` request to `/devices/Fan`.

Make sure you test:
- Success paths (e.g., device exists)
- Error paths (e.g., device doesn’t exist, or already added)

---
```
