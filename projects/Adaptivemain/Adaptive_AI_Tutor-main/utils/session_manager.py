import os
import json

DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "user_profile.json")

def load_all_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)
    
def save_all_users(users):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def load_user_profile(username):
    users = load_all_users()
    if username not in users:
        users[username] = {} #Initialize new user profile if not exists
        save_all_users(users)
    return users[username]

def save_user_profile(username, profile):
    users = load_all_users()
    users[username] = profile
    save_all_users(users)