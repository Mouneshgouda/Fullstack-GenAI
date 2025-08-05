#Optional:Local fallback concepts if AI is not available
LESSONS = {
    "Math": [
        {
            "title": "Addition Basics",
            "content": "Addition is combining two numbers. Example: 2 + 3 = 5."
        },
        {
            "title": "Subtraction Basics",
            "content": "Subtraction is taking away from a number. Example: 5 - 2 = 3."
        }
    ],
    "Science": [
        {
            "title": "States of Matter",
            "content": "Solid, Liquid, and Gas are the three states of matter."
        }
    ]
}

def get_lesson(subject):
    if subject in LESSONS:
        return LESSONS[subject][0]["content"]
    else:
        return "No content available. Please try another subject."