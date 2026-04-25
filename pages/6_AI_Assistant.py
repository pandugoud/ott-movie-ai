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
    <h3 style="margin-top:0;">Ask for suggestions</h3>
    <p class="small-note">
        Example: action movies, sci-fi movies, romance picks, trending trailers
    </p>
</div>
""", unsafe_allow_html=True)

query = st.text_input("Ask AI Assistant")

if query:
    q = query.lower()

    if "action" in q:
        st.success("Recommended: Avengers, Dark Knight, Bahubali, RRR")
    elif "sci" in q or "science" in q:
        st.success("Recommended: Inception, Interstellar, Avatar, The Matrix")
    elif "romance" in q or "love" in q:
        st.success("Recommended: Titanic")
    elif "trending" in q or "top" in q:
        st.success("Trending picks: Inception, Interstellar, Avengers")
    else:
        st.info("Try asking genre-based recommendations like action, sci-fi, or romance.")
