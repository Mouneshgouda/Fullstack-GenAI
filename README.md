~~~python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import gradio as gr

# ===================
# 1. Load & preprocess data
# ===================
df = pd.read_csv("Salary Data.csv")

import missingno as msno

msno.bar(df)
plt.show()

msno.matrix(df)
plt.show()

import plotly.express as px
px.pie(df, names="Gender")

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)  # numeric
df.fillna(df.mode().iloc[0], inplace=True)  # categorical

# Drop duplicates
df.drop_duplicates(inplace=True)

# Boxplots for outliers
for column in df.select_dtypes(include='number').columns:
    plt.figure()
    df.boxplot(column=column)
    plt.title(f'Boxplot of {column}')
    plt.show()

# Separate features & target
X = df.drop("Salary", axis=1)
y = df["Salary"]

# One-hot encode categorical features
X = pd.get_dummies(X, columns=['Gender', 'Education Level', 'Job Title'], drop_first=True)


# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===================
# 2. Train & save model
# ===================
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

print("R² Score:", model.score(X_test, y_test))


joblib.dump(X.columns, "salary_columns.pkl")
joblib.dump(scaler, "salary_scaler.pkl")
joblib.dump(model, "ad_salary.pkl")


# ===================
# 3. Gradio Interface
# ===================
# Load objects
model = joblib.load("ad_salary.pkl")
scaler = joblib.load("salary_scaler.pkl")
columns = joblib.load("salary_columns.pkl")

def predict_salary(years_exp, gender, education, job_title):
    # Create DataFrame from inputs
    data = pd.DataFrame({
        "YearsExperience": [years_exp],
        "Gender": [gender],
        "Education Level": [education],
        "Job Title": [job_title]
    })

    # One-hot encode and match training columns
    data_encoded = pd.get_dummies(data, columns=['Gender', 'Education Level', 'Job Title'], drop_first=True)
    data_encoded = data_encoded.reindex(columns=columns, fill_value=0)

    # Scale
    data_scaled = scaler.transform(data_encoded)

    # Predict
    pred_salary = model.predict(data_scaled)[0]
    return f"Predicted Salary: ${pred_salary:,.2f}"

# Simple UI
demo = gr.Interface(
    fn=predict_salary,
    inputs=[
        gr.Number(label="Years of Experience"),
        gr.Dropdown(["Male", "Female"], label="Gender"),
        gr.Dropdown(["High School", "Bachelor's", "Master's", "PhD"], label="Education Level"),
        gr.Dropdown(["Data Scientist", "Software Engineer", "Manager", "Analyst"], label="Job Title")
    ],
    outputs="text",
    title="Salary Prediction App"
)

demo.launch()

~~~


https://medium.com/@mouneshpatil001/evaluation-metrics-for-classification-models-ec7c3019c248









```
import express from 'express';

const app = express();
const port = 3000;

app.use(express.json());

// 🧪 Dummy in-memory data
let users = [
  {
    id: 1,
    name: 'Mounesh Goud',
    email: 'mounesh@example.com'
  }
];

let nextId = 2; // since 1 is already used

// ➕ Create - POST /users
app.post('/users', (req, res) => {
  const { name, email } = req.body;
  const newUser = { id: nextId++, name, email };
  users.push(newUser);
  res.status(201).json(newUser);
});

// 📥 Read All - GET /users
app.get('/users', (req, res) => {
  res.json(users);
});

// 📥 Read One - GET /users/:id
app.get('/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: 'User not found' });
  res.json(user);
});

// ✏️ Update - PUT /users/:id
app.put('/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: 'User not found' });

  const { name, email } = req.body;
  if (name) user.name = name;
  if (email) user.email = email;

  res.json(user);
});

// ❌ Delete - DELETE /users/:id
app.delete('/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ message: 'User not found' });

  const deletedUser = users.splice(index, 1)[0];
  res.json(deletedUser);
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

```

# Fullstack-GenAI
A full-stack web application integrating GenAI (Generative AI) features using React, Node.js, and Express. Built to demonstrate end-to-end AI-powered solutions.
