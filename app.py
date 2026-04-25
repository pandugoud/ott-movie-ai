import streamlit as st
from src.ui import inject_css, render_sidebar, hero_section
from src.utils import initialize_session

st.set_page_config(
    page_title="OTT Stream Pro Max",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_session()
inject_css()
render_sidebar()

st.title("🎬 OTT STREAM PRO MAX")
hero_section()

st.markdown("""
<div class="glass-card">
    <h3 style="margin-top:0;">Welcome</h3>
    <p class="small-note">
        This is a production-ready Streamlit OTT movie platform starter with a premium
        dark UI inspired by Netflix, Prime Video, and Hotstar.
        Open the sidebar and navigate through Home, Explore, AI Recommender,
        Watchlist, Analytics, and AI Assistant.
    </p>
</div>
""", unsafe_allow_html=True)
