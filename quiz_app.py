import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    /* Header styling */
    .header {
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    /* Card styling for questions */
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    /* Progress bar styling */
    .stProgress > div > div > div {
        background-color: #4CAF50;
    }
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 10px;
        margin-top: 20px;
        font-size: 14px;
        color: #777;
    }
    </style>
    """, unsafe_allow_html=True)

# Define the quiz questions, options, and correct answers
quiz_questions = [
    {
        "question": "What is the output of `print(type([]))` in Python?",
        "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which of the following is used to create a virtual environment in Python?",
        "options": ["virtualenv", "pipenv", "venv", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What does the `__init__` method do in a Python class?",
        "options": ["Initializes the class attributes", "Destroys the class instance", "Imports modules", "None of the above"],
        "answer": "Initializes the class attributes"
    },
    {
        "question": "Which of the following is NOT a valid Python data type?",
        "options": ["int", "float", "char", "str"],
        "answer": "char"
    },
    {
        "question": "What is the result of `2 ** 3` in Python?",
        "options": ["6", "8", "9", "16"],
        "answer": "8"
    }
]

# Initialize session state for user answers, current question, and score
if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * len(quiz_questions)
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_complete" not in st.session_state:
    st.session_state.quiz_complete = False

# Function to display the current question
def display_question():
    question_data = quiz_questions[st.session_state.current_question]
    st.markdown(f"""
        <div class="card">
            <h3>Question {st.session_state.current_question + 1}: {question_data['question']}</h3>
        </div>
    """, unsafe_allow_html=True)
    user_answer = st.radio(
        "Select an option:",
        question_data["options"],
        key=f"question_{st.session_state.current_question}"
    )
    st.session_state.user_answers[st.session_state.current_question] = user_answer

    # Progress bar
    progress = (st.session_state.current_question + 1) / len(quiz_questions)
    st.progress(progress)

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.current_question > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_question -= 1
                st.rerun()
    with col2:
        if st.session_state.current_question < len(quiz_questions) - 1:
            if st.button("Next ➡️"):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("Submit Quiz ✅"):
                calculate_score()
                st.session_state.quiz_complete = True
                st.rerun()

# Function to calculate the score
def calculate_score():
    st.session_state.score = 0
    for i, question in enumerate(quiz_questions):
        if st.session_state.user_answers[i] == question["answer"]:
            st.session_state.score += 1

# Function to display results
def display_results():
    st.success(f"🎉 Quiz submitted! Your score is **{st.session_state.score}/{len(quiz_questions)}**.")
    st.write("### 📝 Review your answers:")
    for i, question in enumerate(quiz_questions):
        st.markdown(f"""
            <div class="card">
                <p><b>Question {i + 1}:</b> {question['question']}</p>
                <p>Your Answer: {st.session_state.user_answers[i]}</p>
                <p>Correct Answer: <b>{question['answer']}</b></p>
            </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 Restart Quiz"):
        st.session_state.user_answers = [None] * len(quiz_questions)
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.rerun()

# Main app logic
def main():
    # Header
    st.markdown("""
        <div class="header">
            <h1>Growth Mindset Challenge 🌱</h1>
            <h2>Python Quiz App 🐍</h2>
            <p>Welcome to the Python Quiz! Test your knowledge with this interactive quiz.</p>
        </div>
    """, unsafe_allow_html=True)

    if not st.session_state.quiz_complete:
        display_question()
    else:
        display_results()

    # Footer
    st.markdown("""
        <div class="footer">
            <p>Developed by ❤️ Sumayya Fazal Hussain</p>
        </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()