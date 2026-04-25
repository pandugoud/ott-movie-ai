import streamlit as st
from src.ui import inject_css, render_sidebar, topbar
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

topbar()

st.markdown("""
<div class="glass-card">
    <h2 style="margin-top:0;">Welcome</h2>
    <p class="mini-note">
        Home page lo featured cinematic banner, large popup trailer, and full OTT detail page untayi.
        Sidebar nundi Home open chesi premium experience chudandi.
    </p>
</div>
""", unsafe_allow_html=True)
