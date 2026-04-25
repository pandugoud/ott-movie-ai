import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --bg: #08131f;
        --bg-soft: #10202f;
        --card: #12263a;
        --card-2: #0f2234;
        --text: #edf6f9;
        --muted: #a7bac7;
        --line: rgba(255,255,255,0.08);
        --primary: #2a9d8f;
        --primary-hover: #23867a;
        --primary-soft: #1f7f74;
        --accent: #e9c46a;
        --shadow: 0 16px 36px rgba(0,0,0,0.28);
        --shadow-2: 0 10px 24px rgba(0,0,0,0.22);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text);
    }

    .stApp {
        background-color: var(--bg);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(8, 19, 31, 0.88);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }

    [data-testid="stSidebar"] {
        background: var(--bg-soft);
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] * {
        color: var(--text) !important;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 2.2rem;
        padding-bottom: 2rem;
    }

    .topbar {
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding: 0.9rem 0 1.2rem 0;
    }

    .brand-logo {
        font-size: 1.35rem;
        font-weight: 900;
        letter-spacing: -0.04em;
        color: var(--text);
    }

    .brand-logo span {
        color: var(--primary);
    }

    .compact-note {
        color: var(--muted);
        font-size: 0.92rem;
    }

    .hero-v2 {
        border-radius: 24px;
        padding: 1.35rem;
        background-color: var(--bg-soft);
        border: 1px solid var(--line);
        box-shadow: var(--shadow);
        margin-bottom: 1.2rem;
        height: 100%;
    }

    .hero-pills {
        display:flex;
        gap:0.55rem;
        flex-wrap:wrap;
        margin-bottom: 1rem;
    }

    .hero-pill {
        padding: 0.42rem 0.82rem;
        border-radius: 999px;
        background: rgba(42,157,143,0.12);
        border: 1px solid rgba(42,157,143,0.24);
        font-size: 0.74rem;
        font-weight: 800;
        color: #dff7f3;
    }

    .hero-title {
        font-size: 3.2rem;
        line-height: 1.02;
        font-weight: 900;
        letter-spacing: -0.05em;
        margin-bottom: 0.75rem;
        color: var(--text);
    }

    .hero-title .accent {
        color: var(--primary);
    }

    .hero-desc {
        font-size: 1rem;
        line-height: 1.8;
        color: var(--muted) !important;
        margin-bottom: 1rem;
    }

    .hero-meta {
        display:flex;
        gap:0.6rem;
        flex-wrap:wrap;
        margin-bottom: 1rem;
    }

    .meta-chip {
        padding: 0.46rem 0.78rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        font-size: 0.84rem;
        color: var(--text);
    }

    .hero-poster-box {
        background-color: var(--card);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 0.85rem;
        box-shadow: var(--shadow-2);
        height: 100%;
    }

    .section-title {
        font-size: 1.16rem;
        font-weight: 800;
        margin: 1rem 0 0.25rem 0;
        letter-spacing: -0.02em;
        color: var(--text);
    }

    .section-sub {
        color: var(--muted) !important;
        margin-bottom: 0.9rem;
        font-size: 0.92rem;
    }

    .grid-card {
        background-color: var(--card-2);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 20px;
        padding: 0.9rem;
        box-shadow: var(--shadow-2);
        overflow: hidden;
        margin-bottom: 0.8rem;
    }

    .movie-title {
        font-size: 0.98rem;
        font-weight: 800;
        margin-top: 0.1rem;
        line-height: 1.25;
        color: var(--text);
    }

    .movie-sub {
        color: var(--muted) !important;
        font-size: 0.83rem;
        margin-top: 0.18rem;
        margin-bottom: 0.65rem;
    }

    .mini-stat {
        color: var(--accent) !important;
        font-weight: 700;
    }

    .watch-chip {
        display:inline-block;
        padding:0.36rem 0.7rem;
        border-radius:999px;
        background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.08);
        font-size:0.78rem;
        margin-right:0.4rem;
        margin-bottom:0.4rem;
        color:var(--text);
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid rgba(42,157,143,0.28);
        color: #ffffff;
        font-weight: 800;
        padding: 0.74rem 0.95rem;
        background-color: var(--primary);
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
        font-size: 0.9rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: var(--primary-hover);
        color: #ffffff;
        border-color: rgba(42,157,143,0.40);
    }

    .stButton > button:focus {
        color: #ffffff;
        box-shadow: 0 0 0 0.18rem rgba(42,157,143,0.20);
    }

    input, textarea, .stTextInput input {
        color: var(--text) !important;
        background-color: #0e1d2c !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #0e1d2c !important;
        color: var(--text) !important;
    }

    @media (max-width: 640px) {
        .topbar {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.35rem;
            padding: 0.7rem 0 1rem 0;
        }

        .block-container {
            padding-top: 1.6rem;
            padding-bottom: 1.5rem;
        }

        .hero-title {
            font-size: 2.1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="padding:0.35rem 0 0.9rem 0;">
            <div style="font-size:1.2rem;font-weight:900;color:#edf6f9;">🎬 OTT Stream Pro Max</div>
            <div style="color:#a7bac7;margin-top:0.35rem;">
                Premium movie discovery UI with mood-based recommendations
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.info("Simple rich colors updated.")


def topbar():
    st.markdown("""
    <div class="topbar">
        <div class="brand-logo"><span>OTT Stream Pro Max</span></div>
        <div class="compact-note">Premium OTT-inspired movie browsing</div>
    </div>
    """, unsafe_allow_html=True)


def section_header(title, sub=None):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<div class="section-sub">{sub}</div>', unsafe_allow_html=True)


def movie_card(title, genre, overview):
    st.markdown(f"""
    <div class="grid-card">
        <div class="movie-title">{title}</div>
        <div class="movie-sub">{genre}</div>
        <div style="color:#a7bac7; font-size:0.9rem; line-height:1.6;">
            {overview}
        </div>
    </div>
    """, unsafe_allow_html=True)
