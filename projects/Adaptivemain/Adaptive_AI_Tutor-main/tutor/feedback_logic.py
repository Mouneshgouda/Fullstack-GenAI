import os
import json

QUIZ_LOG_FILE = os.path.join("data", "quiz_results.json")

LEVELS = ["beginner", "intermediate", "advanced"]

def update_performance(profile, subject, result):
    # Initialize progress tracker
    profile.setdefault("progress", {}).setdefault(subject, []).append({
        "score": result["score"],
        "correct": result["correct"]
    })

    # Initialize difficulty level tracker
    level = profile.setdefault("levels", {}).get(subject, "beginner")
    level_index = LEVELS.index(level)

    # Calculate average score
    scores = [x["score"] for x in profile["progress"][subject]]
    avg_score = sum(scores) / len(scores)

    # Adjust perceived grades based on score trends
    original_grade = profile["grades"].get(subject, 70)
    if avg_score > 90 and original_grade < 70:
        profile["grades"][subject] = min(100, original_grade + 10)
    elif avg_score < 50 and original_grade > 70:
        profile["grades"][subject] = max(0, original_grade - 10)

    # Adjust difficulty level
    if avg_score >= 90 and level_index < len(LEVELS) - 1:
        profile["levels"][subject] = LEVELS[level_index + 1]
    elif avg_score <= 50 and level_index > 0:
        profile["levels"][subject] = LEVELS[level_index - 1]

    # Log quiz result to global quiz history
    log_quiz(profile.get("name", "unknown_user"), subject, result)

def log_quiz(username, subject, result):
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(QUIZ_LOG_FILE):
        quiz_log = {}
    else:
        with open(QUIZ_LOG_FILE, "r") as f:
            try:
                quiz_log = json.load(f)
            except json.JSONDecodeError:
                quiz_log = {}

    quiz_log.setdefault(username, {}).setdefault(subject, []).append(result)

    with open(QUIZ_LOG_FILE, "w") as f:
        json.dump(quiz_log, f, indent=4)