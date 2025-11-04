import streamlit as st

def clean_session_questions():
    for key in ["perguntas", "index", "respostas"]:
        if key in st.session_state:
            del st.session_state[key]