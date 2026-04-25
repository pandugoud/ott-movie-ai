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
<div style="padding:1rem;border:1px solid rgba(255,255,255,0.08);border-radius:20px;background:rgba(255,255,255,0.03);">
    <h2 style="margin-top:0;">Welcome</h2>
    <p style="color:#9aa8c3;">
        Sidebar nundi Home page open cheyyandi. Akkada premium hero, trailer popup, and full OTT detail page untayi.
    </p>
</div>
""", unsafe_allow_html=True)
