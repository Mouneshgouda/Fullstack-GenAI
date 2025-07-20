

## 🧱 What You Need First
 ✅ 1. Jenkins Installed
 ``  python
- On your computer or a server.
- 👉 Go to https://www.jenkins.io/download/ and install it.

```
 ✅ 2. GitHub Account
```python
- And a repository with your project code.
```

### 🔧 Step-by-Step Guide

```python
- 🟢 Step 1: Create GitHub Repository
- Go to https://github.com

- Click "New Repository"

- Give it a name like my-first-pipeline

- Add a file like main.py or index.html or your app files

- 🟢 Step 2: Open Jenkins in your browser
- Usually runs at: http://localhost:8080
- (or your server IP: http://your-ip:8080)

🟢 Step 3: Create a Freestyle Project in Jenkins
- On Jenkins dashboard → click “New Item”

- Enter project name: my-first-job

- Select “Freestyle project”

Click OK

🟢 Step 4: Link Your GitHub Repo to Jenkins
- Scroll to Source Code Management

- Select Git

- Paste your GitHub repo URL:
- Example:

- https://github.com/your-username/my-first-pipeline.git
- If your repo is private, click Add Credentials and add GitHub username + token

🟢 Step 5: Add Build Steps
- Scroll to Build

- Click “Add build step” → “Execute shell”

- Example: If your repo has a simple Python script:


- echo "Running my app"
- python3 main.py
- 🟢 Step 6: Save and Run
- Click Save

- On left sidebar, click “Build Now”

- Go to Console Output to see what happened
```
