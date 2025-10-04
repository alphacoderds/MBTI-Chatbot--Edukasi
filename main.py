import streamlit as st
from quiz import run_quiz
from chatbot import run_chatbot

st.set_page_config(page_title="MBTI Chatbot Edukasi", page_icon="🤖")

st.title("💬 MBTI Chatbot Edukasi")

# State awal
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False
if "mbti_result" not in st.session_state:
    st.session_state.mbti_result = None

if not st.session_state.quiz_done:
    run_quiz()
else:
    st.success(f"Kamu sudah menyelesaikan kuis. Hasil: **{st.session_state.mbti_result}**")
    run_chatbot()
