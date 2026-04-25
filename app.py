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
        Ee version lo image place lo video play support undi.
        Poster click cheste kuda trailer play avvachu, normal play button tho kuda open cheyyachu.
    </p>
</div>
""", unsafe_allow_html=True)
