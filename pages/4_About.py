import streamlit as st
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session

st.set_page_config(
    page_title="About Us | OTT Stream Pro Max",
    page_icon="ℹ️",
    layout="wide"
)

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
        We help users discover the <span class="accent">right movie</span> at the right time
    </div>
    <div class="hero-desc">
        OTT Stream Pro Max is designed to make movie discovery simple, stylish, and personalized.
        Users can explore trending films, search by genre or language, save favorites to a watchlist,
        and get smart recommendations based on mood and movie similarity.
    </div>
</div>
""", unsafe_allow_html=True)

section_header("Who We Are", "A premium movie discovery platform")
col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown("""
    <div class="grid-card">
        <div class="movie-title" style="font-size:1.1rem;">Our Mission</div>
        <div class="movie-sub">Smart and simple movie selection</div>
        <div style="color:#a7bac7; line-height:1.8; font-size:0.95rem;">
            We want to reduce endless scrolling and help users quickly find something worth watching.
            Instead of browsing randomly, users can discover movies through a clean OTT-style interface,
            intelligent filtering, and recommendation logic that feels fast and useful.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="grid-card">
        <div class="movie-title" style="font-size:1.1rem;">What Makes Us Different</div>
        <div class="movie-sub">Built for a smoother entertainment experience</div>
        <div style="color:#a7bac7; line-height:1.8; font-size:0.95rem;">
            Our app combines premium UI styling, mood-based movie discovery, title-based recommendations,
            watchlist support, and quick trailer access. The goal is to make the experience feel closer
            to a modern OTT platform rather than a basic movie list.
        </div>
    </div>
    """, unsafe_allow_html=True)

section_header("What We Offer", "Core platform highlights")
f1, f2, f3 = st.columns(3, gap="large")

with f1:
    st.markdown("""
    <div class="grid-card">
        <div class="movie-title">🎬 Smart Discovery</div>
        <div class="movie-sub">Search by title, genre, year, language</div>
        <div style="color:#a7bac7; line-height:1.7; font-size:0.9rem;">
            Find movies faster with a clean explore page and better browsing experience.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="grid-card">
        <div class="movie-title">🤖 AI Recommendations</div>
        <div class="movie-sub">Mood based and similarity based suggestions</div>
        <div style="color:#a7bac7; line-height:1.7; font-size:0.9rem;">
            Users can get movie suggestions based on personal mood or a selected favorite movie.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="grid-card">
        <div class="movie-title">❤️ Watchlist & Trailers</div>
        <div class="movie-sub">Save now, watch later</div>
        <div style="color:#a7bac7; line-height:1.7; font-size:0.9rem;">
            Save interesting titles, open detail pages, and watch trailers without leaving the app.
        </div>
    </div>
    """, unsafe_allow_html=True)

section_header("Our Vision", "Future improvements")
st.markdown("""
<div class="grid-card">
    <div class="movie-title" style="font-size:1.08rem;">Where this platform can grow</div>
    <div class="movie-sub">The next version can become even more powerful</div>
    <div style="color:#a7bac7; line-height:1.85; font-size:0.95rem;">
        In future versions, this app can be expanded with live OTT integrations, user authentication,
        personalized recommendation history, language-first browsing, trending analytics, and richer
        content insights like ratings, cast, reviews, and streaming availability.
    </div>
</div>
""", unsafe_allow_html=True)

section_header("Quick Navigation", "Move to other pages")
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
