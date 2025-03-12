import streamlit as st
import random
import time


st.title("📝Quiz Appilication")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]

if "current_questions" not in st.session_state:
    st.session_state.current_questions = random.choice(questions)

question = st.session_state.current_questions

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅Correct!")
        st.balloons()
    else:
        st.error("❌Incorrect! The correct answer is " + question["answer"])
    
    time.sleep(2)

    st.session_state.current_questions = random.choice(questions)

    st.rerun()