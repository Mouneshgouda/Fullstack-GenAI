# 🚀 Git Commands Guide for VS Code Project (`main.py` & `learning.txt`)

---

## 🔧 Initial Setup (One Time per Project)

### Initialize Git in the folder:
```bash
git init
```

### Configure identity (if not done globally):

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

---

## 📥 Staging and Committing Files

### Add specific files to staging:
```bash
git add main.py learning.txt
```

### Or add everything:
```bash
git add .
```

### Commit staged changes:
```bash
git commit -m "Initial commit with main.py and learning.txt"
```

---

## 🔁 Checking History and Changes

### See commit history:
```bash
git log
```
➡️ *Exit `git log` by pressing `q`*

### See what changed in files:
```bash
git diff
```

---

## ⏪ Undoing Changes

### Unstage a file (but keep the changes):
```bash
git reset main.py
```

### Discard changes in a file (⚠ irreversible):
```bash
git checkout -- learning.txt
```

---

## 🌐 Working with Remote (e.g., GitHub)

### Add a remote repository:
```bash
git remote add origin https://github.com/yourusername/yourrepo.git
```

### Push commits to GitHub:
```bash
git push -u origin master
```

### Pull latest changes from remote:
```bash
git pull origin master
```

---

## 🆕 Working with Branches

### Create and switch to a new branch:
```bash
git checkout -b new-feature
```

### Switch to an existing branch:
```bash
git checkout master
```

### Merge a branch into master:
```bash
git merge new-feature
```

---

## 🧪 Stashing Work (Temporary Save)

### Save uncommitted changes:
```bash
git stash
```

### Reapply stashed changes:
```bash
git stash apply
```

---

## 🧹 Cleaning and Resetting

### Remove untracked files:
```bash
git clean -f
```

### Hard reset to last commit:
```bash
git reset --hard
```

---

## 🧭 Viewing More Info

### See list of branches:
```bash
git branch
```

### Show a summary of recent commits:
```bash
git log --oneline --graph --all
```

---

## ✅ Recommended Flow (Example)

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/yourrepo.git
git push -u origin master
```

---

> Use this guide directly in your VS Code terminal to manage Git for your project smoothly!
