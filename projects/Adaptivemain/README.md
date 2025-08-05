# Adaptive AI Tutor

An intelligent tutoring system that adapts to individual student needs using Google's Gemini AI model for personalized learning experiences.

## Features

### 1. Personalized Learning Experience
- **Education Level Support**
  - College level learning
  - School grades (1-12) with specialized curricula
  - Stream-specific subjects for grades 11-12 (Science, Commerce, Humanities)

### 2. Smart Content Generation
- **AI-Powered Teaching**
  - Dynamic concept explanations
  - Grade-appropriate content
  - Difficulty adjustment based on performance
  - Non-repetitive topic selection

- **Adaptive Quizzes**
  - Customizable number of questions (3-10)
  - Multiple choice format
  - Difficulty adapts to student marks
  - Immediate feedback and scoring

### 3. Progress Tracking
- Subject-wise performance monitoring
- Quiz history and scores
- Learning pattern analysis
- Performance-based difficulty adjustment

## Project Structure

```
├── app.py                  # Main application entry point
├── pages/                  # Application pages
│   ├── Home.py            # Main learning interface
│   ├── Performance.py     # Progress tracking view
│   └── Settings.py        # User settings management
├── tutor/                 # Core tutoring logic
│   ├── ai_tutor.py       # AI teaching component (Gemini)
│   ├── quiz_engine.py    # Quiz generation & evaluation
│   ├── feedback_logic.py # Performance analysis
│   └── knowledge_base.py # Backup content storage
├── utils/                 # Utilities
│   └── session_manager.py # User data management
└── data/                  # Data storage
    ├── user_profile.json  # User profiles and settings
    └── quiz_results.json  # Quiz history and scores
```

## Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0
- **Data Storage**: JSON-based local storage
- **Language**: Python 3.11+

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\Activate
```

3. Install dependencies:
```bash
pip install streamlit google-generativeai
```

4. Set up Google Gemini API key:
   - Get your API key from Google AI Studio
   - Set it in ai_tutor.py or as an environment variable

5. Run the application:
```bash
streamlit run app.py
```

## Usage Guide

### 1. Initial Setup
- Enter your name
- Select education level (School/College)
- For school students:
  - Select grade (1-12)
  - For grades 11-12, choose stream (Science/Commerce/Humanities)
  - Enter marks for predefined subjects
- For college students:
  - Add custom subjects
  - Enter current proficiency levels

### 2. Learning Mode
- Select a subject to study
- Click "Teach me a concept" for new topics
- Content difficulty adapts to your marks
- Take quizzes to test understanding
- View immediate feedback and scores

### 3. Performance Tracking
- Monitor subject-wise progress
- View quiz history
- Track improvement over time

### 4. Settings
- Modify subjects
- Update marks
- Adjust learning preferences

## Features in Detail

### Adaptive Learning System
- Content difficulty based on:
  - Education level
  - Grade/Stream
  - Subject marks
  - Quiz performance

### Smart Quiz System
- Question generation based on:
  - Previously taught concepts
  - Current performance level
  - Grade-appropriate content
- Interactive answering with validation
- Comprehensive feedback

### Progress Management
- JSON-based data persistence
- Individual user profiles
- Subject-wise tracking
- Performance history

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License

MIT License - Feel free to use and modify for your needs.

## Acknowledgments

- Built with Streamlit
- Powered by Google Gemini AI
- Educational content aligned with standard curricula
