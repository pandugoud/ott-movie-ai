import streamlit as st
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session

st.set_page_config(page_title="About Us | OTT Stream Pro Max", page_icon="ℹ️", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">ABOUT US</span>
        <span class="hero-pill">OTT EXPERIENCE</span>
        <span class="hero-pill">MOVIE DISCOVERY</span>
    </div>
    <div class="hero-title">
        A cleaner way to discover the <span class="accent">right movie</span>
    </div>
    <div class="hero-desc">
        OTT Stream Pro Max is designed to make movie discovery feel stylish, simple, and helpful through premium UI, smarter recommendations, and quick access flows.
    </div>
</div>
""", unsafe_allow_html=True)

section_header("Who We Are", "Platform overview")
c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown("""
    <div class="panel-card">
        <div class="movie-title" style="font-size:1.08rem;">Our Mission</div>
        <div class="movie-sub">Smarter entertainment discovery</div>
        <div style="color:#91a4b7; line-height:1.8; font-size:0.94rem;">
            The goal is to reduce endless scrolling and help users quickly find movies worth watching through search, recommendation logic, and premium OTT-inspired presentation.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="panel-card">
        <div class="movie-title" style="font-size:1.08rem;">Why This App</div>
        <div class="movie-sub">Built for a better browsing feel</div>
        <div style="color:#91a4b7; line-height:1.8; font-size:0.94rem;">
            The app brings together search, AI-style recommendations, trailer viewing, analytics, and watchlist support inside one richer movie exploration interface.
        </div>
    </div>
    """, unsafe_allow_html=True)

section_header("What We Offer", "Core strengths")
f1, f2, f3 = st.columns(3, gap="large")
with f1:
    st.markdown("""
    <div class="panel-card">
        <div class="movie-title">🎬 Smart Discovery</div>
        <div class="movie-sub">Search by title, genre, language, year</div>
        <div style="color:#91a4b7; line-height:1.75; font-size:0.9rem;">
            Users can browse movies quickly using a clean and structured content grid.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="panel-card">
        <div class="movie-title">🤖 Recommendation Engine</div>
        <div class="movie-sub">Mood-based and title-based suggestions</div>
        <div style="color:#91a4b7; line-height:1.75; font-size:0.9rem;">
            The platform suggests matching content based on user mood or selected movie similarity.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="panel-card">
        <div class="movie-title">❤️ Save & Watch</div>
        <div class="movie-sub">Watchlist and trailer-first experience</div>
        <div style="color:#91a4b7; line-height:1.75; font-size:0.9rem;">
            Save interesting movies, open rich detail pages, and watch trailers directly.
        </div>
    </div>
    """, unsafe_allow_html=True)

section_header("Quick Navigation", "Move across the platform")
n1, n2, n3, n4 = st.columns(4, gap="small")
with n1:
    if st.button("🏠 Home", key="about_home", width="stretch"):
        st.switch_page("pages/1_Home.py")
with n2:
    if st.button("🔎 Explore", key="about_explore", width="stretch"):
        st.switch_page("pages/2_Explore.py")
with n3:
    if st.button("🤖 AI Recommender", key="about_ai", width="stretch"):
        st.switch_page("pages/3_AI_Recommender.py")
with n4:
    if st.button("❤️ Watchlist", key="about_watchlist", width="stretch"):
        st.switch_page("pages/5_Watchlist.py")
