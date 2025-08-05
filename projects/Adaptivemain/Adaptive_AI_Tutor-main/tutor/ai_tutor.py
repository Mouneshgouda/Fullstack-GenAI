import google.generativeai as genai

# Gemini setup (assumes key is set via environment variable or earlier configuration)
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")

def get_difficulty_level(marks):
    if marks >= 80:
        return "advanced"
    elif marks >= 60:
        return "intermediate"
    else:
        return "basic"

def teach_concept(subject, taught_concepts=None, grade=None, marks=None):
    if taught_concepts is None:
        taught_concepts = []

    difficulty = get_difficulty_level(marks) if marks is not None else "intermediate"
    grade_context = f"for {grade}" if grade else "at college level"
    
    prompt = f"""
    You are an expert {subject} teacher.
    
    Generate a {difficulty}-level concept explanation about a SPECIFIC topic within {subject} 
    that has NOT been covered in these previous concepts: {taught_concepts}
    
    The content should be appropriate {grade_context}.
    
    For {difficulty} level (student's current grade: {marks}%):
    - Basic level: Focus on fundamental concepts with simple examples
    - Intermediate level: Include more detailed explanations and practical applications
    - Advanced level: Cover complex topics and challenging examples
    
    Choose from core curriculum topics in {subject}, ensuring each new concept builds upon previous knowledge.
    
    Important: Each concept should cover a DIFFERENT fundamental topic, not just a different perspective on the same topic.
    
    Your response should include:
    - Main Concept Name (as a clear, specific topic heading)
    - A brief, intuitive explanation appropriate for {difficulty} level
    - One example matching the student's level
    - Keep it interactive and engaging if possible
    NOTE: You cannot start with Ok let's dive in or Let's start with this today as the first line. The first line should be the topic name only.
    """
    response = model.generate_content(prompt)
    return response.text
