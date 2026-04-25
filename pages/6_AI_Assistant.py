import streamlit as st
from src.ui import inject_css, render_sidebar
from src.utils import initialize_session

st.set_page_config(page_title="AI Assistant | OTT Stream Pro Max", page_icon="💬", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("💬 AI Assistant")

st.markdown("""
<div class="glass-card">
    <h3 style="margin-top:0;">Assistant Mode</h3>
    <p class="small-note">
        This starter version uses rule-based replies. You can later upgrade it with OpenAI API integration.
    </p>
</div>
""", unsafe_allow_html=True)

query = st.text_input("Ask something like: suggest action movies, sci-fi picks, family movies")

if query:
    q = query.lower()

    if "action" in q:
        st.success("Try: Avengers, Dark Knight, Bahubali, RRR")
    elif "sci-fi" in q or "scifi" in q or "science" in q:
        st.success("Try: Inception, Interstellar, Avatar, The Matrix")
    elif "romance" in q or "love" in q:
        st.success("Try: Titanic")
    else:
        st.info("Try asking for genres like action, sci-fi, romance, or trending movies.")
