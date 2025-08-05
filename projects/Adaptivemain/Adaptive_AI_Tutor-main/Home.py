import streamlit as st
import json
import os

from utils.session_manager import load_user_profile, save_user_profile
from tutor.ai_tutor import teach_concept
from tutor.quiz_engine import generate_quiz, evaluate_answers
from tutor.feedback_logic import update_performance

DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "user_profile.json")
os.makedirs(DATA_DIR, exist_ok=True)

#---------------UI Components----------------

def get_user_name():
    return st.text_input("Enter your name:", key="username")

def get_user_grades():
    st.subheader("Enter your subjects and marks")

    subjects = {}
    num_subjects = st.number_input("How many subjects do you want to enter?", min_value=1, max_value=20, value=3)

    with st.form("subjects_form"):
        for i in range(int(num_subjects)):
            col1, col2 = st.columns(2)
            with col1:
                subject = st.text_input(f"Subject {i + 1} Name:", key=f"subject_{i}")
            with col2:
                marks = st.slider(f"Grade/Marks: ", 0, 100, 75, key=f"marks_{i}")
            if subject:
                subjects[subject] = marks

        submit_button = st.form_submit_button("Save Subjects")

        if submit_button:
            if len(subjects) == 0:
                st.error("Please enter at least one subject name.")
                return None
            return subjects
        
    return None

def select_subject(subjects):
    return st.selectbox("Select a subject to learn:", list(subjects))

def get_education_level():
    education_level = st.radio("Select your education level:", ["College", "School"])
    if education_level == "School":
        grade = st.selectbox("Select your grade:", 
                           ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5",
                            "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10",
                            "Grade 11", "Grade 12"])
        return {"level": education_level, "grade": grade}
    return {"level": education_level, "grade": None}

def get_school_subjects(grade):
    # Predefined subjects for each grade
    school_subjects = {
        "Grade 1-5": ["English", "Mathematics", "Science", "Social Studies"],
        "Grade 6-8": ["English", "Mathematics", "Science", "Computer Science", "History", "Geography", "Civics"],
        "Grade 9-10": ["English", "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "Indian History", "Political Science", "Geography", "Economics"]
    }
    
    grade_num = int(grade.split()[1])
    if grade_num <= 5:
        subjects = school_subjects["Grade 1-5"]
    elif grade_num <= 8:
        subjects = school_subjects["Grade 6-8"]
    elif grade_num <= 10:
        subjects = school_subjects["Grade 9-10"]
    else:
        stream = st.selectbox("Select your stream:", ["Science", "Commerce", "Humanities"])
        if stream == "Science":
            subjects = ["English", "Physics", "Chemistry", "Mathematics", "Biology", "Computer Science"]
        elif stream == "Commerce":
            subjects = ["English", "Accounts", "Business Studies", "Business Mathematics", "Economics"]
        else:
            subjects = ["English", "Indian History", "Political Science", "Legal Studies", ""]

    st.subheader("Enter your marks for each subject:")
    grades = {}
    
    with st.form("grades_form"):
        for subject in subjects:
            marks = st.slider(f"Marks in {subject}:", 0, 100, 75, key=f"marks_{subject}")
            grades[subject] = marks
        
        submit = st.form_submit_button("Save Grades")
        if submit:
            return grades
    return None

#-----------------------Main App-----------------------

def run():

    #Step 1: Get User Info
    username = get_user_name()

    if not username:
        st.warning("Please enter your name to continue.")
        return
    
    profile = load_user_profile(username)

    if not profile:
        #New User
        st.success("Welcome, " + username + "! Let's set up your learning profile.")
        
        # Get education level and grade
        education_info = get_education_level()
        
        if education_info["level"] == "School":
            grades = get_school_subjects(education_info["grade"])
        else:
            grades = get_user_grades()  # Original college subject input

        if not grades:
            st.warning("Please enter your marks to continue.")
            return
        
        # Initialize profile with education info
        profile = {
            "name": username,
            "education_level": education_info["level"],
            "grade": education_info["grade"],
            "grades": grades,
            "subjects": list(grades.keys()),
            "progress": {},
            "taught_concepts": {subj: [] for subj in grades.keys()}
        }
        save_user_profile(username, profile)
    else:
        # Ensure taught_concepts exists for existing profiles
        if "taught_concepts" not in profile:
            profile["taught_concepts"] = {subj: [] for subj in profile["subjects"]}
            save_user_profile(username, profile)
        st.success(f"Welcome back, {username}!")

    st.divider()

    #Step 2: Select Subject
    selected_subject = select_subject(profile["grades"])

    #Step 3: Teach a Concept
    col1, col2 = st.columns([3, 1])
    with col1:
        teach_button = st.button(f"Teach me a concept in {selected_subject}")
    with col2:
        reset_button = st.button("Reset Concepts")

    if reset_button:
        profile["taught_concepts"][selected_subject] = []
        save_user_profile(username, profile)
        st.success("Concept history has been reset!")

    if teach_button:
        with st.spinner("Generating concept explanation..."):
            subject_marks = profile["grades"].get(selected_subject, 75)
            explanation = teach_concept(
                selected_subject, 
                profile["taught_concepts"].get(selected_subject, []),
                profile.get("grade"),
                subject_marks
            )
            
            if explanation:
                # Extract concept name from explanation
                concept_name = explanation.split('\n')[0].strip()
                profile["taught_concepts"][selected_subject].append(concept_name)
                save_user_profile(username, profile)
                
                st.markdown("### Concept Explanation")
                st.write(explanation)

                # Show previously taught concepts
                if profile["taught_concepts"][selected_subject]:
                    with st.expander("Previously taught concepts"):
                        for concept in profile["taught_concepts"][selected_subject]:
                            st.write(f"• {concept}")
            else:
                st.error("Failed to generate concept explanation. Please try again.")

    #Step 4: Quiz Time
    st.markdown("### Quick Quiz")
    col1, col2 = st.columns([3, 1])
    with col1:
        quiz_button = st.button(f"Start Quiz in {selected_subject}")
    with col2:
        num_questions = st.number_input("Number of questions:", min_value=3, max_value=10, value=3)

    if quiz_button:
        with st.spinner("Generating quiz..."):
            taught_concepts = profile["taught_concepts"].get(selected_subject, [])
            subject_marks = profile["grades"].get(selected_subject, 75)
            quiz = generate_quiz(
                selected_subject, 
                taught_concepts, 
                num_questions,
                profile.get("grade"),
                subject_marks
            )

        if not quiz:
            st.error("Failed to generate quiz. Please try again later.")
            return
        
        st.session_state.quiz = quiz

    if "quiz" in st.session_state:
        quiz = st.session_state.quiz
        user_answers = {}

        # Create form for quiz submission
        with st.form("quiz_form"):
            for idx, q in enumerate(quiz):
                st.markdown(f"**Q{idx + 1}: {q['question']}**")
                answer = st.radio(
                    "Choose:",
                    options=["Select an option"] + q["options"],
                    key=f"q_{idx}",
                    index=0
                )
                if answer != "Select an option":  # Only add actual answers
                    user_answers[idx] = answer

            submit_button = st.form_submit_button("Submit Quiz")

            if submit_button:
                # Check if all questions are answered
                answered_questions = len(user_answers)
                total_questions = len(quiz)

                if answered_questions < total_questions:
                    st.error(f"Please answer all questions! You have {total_questions - answered_questions} unanswered questions.")
                    return

                result = evaluate_answers(quiz, user_answers)
                st.markdown("### Quiz Results")
                st.success(result["feedback"])

                #Step 5: Feedback Logic
                update_performance(profile, selected_subject, result)
                save_user_profile(username, profile)

                del st.session_state.quiz
