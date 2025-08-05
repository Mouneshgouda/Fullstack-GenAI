import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.0-flash")

def get_difficulty_level(marks):
    if marks >= 80:
        return "advanced"
    elif marks >= 60:
        return "intermediate"
    else:
        return "basic"

def generate_quiz(subject, taught_concepts=None, num_questions=3, grade=None, marks=None):
    if taught_concepts is None:
        taught_concepts = []

    difficulty = get_difficulty_level(marks) if marks is not None else "intermediate"
    concepts_list = ", ".join(taught_concepts) if taught_concepts else "basic concepts"
    grade_context = f"for {grade}" if grade else "at college level"
    
    prompt = f"""
    Generate exactly {num_questions} multiple choice questions (MCQs) for {subject} that specifically test understanding of: {concepts_list}
    
    The questions should be appropriate {grade_context} and at {difficulty} level (student's current grade: {marks}%).

    Difficulty guidelines:
    - Basic level: Focus on recall and simple understanding
    - Intermediate level: Include application and analysis
    - Advanced level: Add complex problem-solving and evaluation

    IMPORTANT: Your response must be ONLY a valid JSON array with this EXACT structure:
    [
        {{
            "question": "Question text here",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Exact text of correct option"
        }}
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Clean up the response to ensure valid JSON
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "")
        
        import json
        quiz_data = json.loads(response_text.strip())
        
        # Validate quiz structure
        if not isinstance(quiz_data, list) or len(quiz_data) != num_questions:
            print(f"Quiz validation failed: Expected {num_questions} questions")
            return None
            
        for q in quiz_data:
            if not all(k in q for k in ("question", "options", "answer")):
                print("Quiz validation failed: Missing required fields")
                return None
            if len(q["options"]) != 4:
                print("Quiz validation failed: Wrong number of options")
                return None
            if q["answer"] not in q["options"]:
                print("Quiz validation failed: Answer not in options")
                return None
                
        return quiz_data
        
    except Exception as e:
        print(f"Quiz generation error: {str(e)}")
        return None

def evaluate_answers(quiz, user_answers):
    correct = 0
    total = len(quiz)

    for i, q in enumerate(quiz):
        if user_answers.get(i) == q['answer']:
            correct += 1

    score = round((correct / total) * 100, 2)
    feedback = f"You got {correct}/{total} correct. Score: {score}%."

    if score == 100:
        feedback += " Excellent work! You're ready for the next level."

    elif score >= 60:
        feedback += " Good job! But review a few concepts before moving on."

    else:
        feedback += " Let's go back and review the topic again."

    return {
        "score": score,
        "correct": correct,
        "feedback": feedback
    }