import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg-main: #0b1020;
        --bg-card: rgba(18, 24, 38, 0.78);
        --bg-card-2: rgba(10, 16, 28, 0.88);
        --text-main: #f5f7fb;
        --text-soft: #aab6d3;
        --red-netflix: #e50914;
        --blue-prime: #00a8e1;
        --hotstar-cyan: #14d9ff;
        --gold-accent: #ffd166;
        --border-soft: rgba(255,255,255,0.10);
        --shadow-main: 0 10px 30px rgba(0,0,0,0.35);
        --grad-brand: linear-gradient(90deg, #e50914 0%, #00a8e1 52%, #14d9ff 100%);
        --grad-card: linear-gradient(135deg, rgba(229,9,20,0.16), rgba(0,168,225,0.12) 55%, rgba(20,217,255,0.10));
    }

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(229,9,20,0.14), transparent 24%),
            radial-gradient(circle at top right, rgba(0,168,225,0.14), transparent 26%),
            radial-gradient(circle at bottom center, rgba(20,217,255,0.08), transparent 20%),
            linear-gradient(180deg, #05070d 0%, #0b1020 35%, #090d18 100%);
        color: var(--text-main);
    }

    [data-testid="stHeader"] {
        background: rgba(5, 8, 15, 0.65);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(7,10,18,0.98) 0%, rgba(10,14,26,0.98) 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    [data-testid="stSidebar"] * {
        color: #eef3ff !important;
    }

    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 2rem;
        max-width: 1350px;
    }

    h1, h2, h3, h4, p, span, label, div {
        color: var(--text-main);
    }

    .hero-wrap {
        position: relative;
        overflow: hidden;
        padding: 2.4rem 2rem;
        border-radius: 24px;
        background:
            linear-gradient(135deg, rgba(229,9,20,0.20) 0%, rgba(10,14,26,0.82) 35%, rgba(0,168,225,0.18) 70%, rgba(20,217,255,0.14) 100%);
        border: 1px solid var(--border-soft);
        box-shadow: var(--shadow-main);
        margin-bottom: 1.2rem;
    }

    .hero-wrap::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.04), transparent);
        transform: translateX(-100%);
        animation: shine 6s linear infinite;
    }

    @keyframes shine {
        100% { transform: translateX(100%); }
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.05;
        margin-bottom: 0.65rem;
        letter-spacing: -0.04em;
    }

    .hero-sub {
        font-size: 1.05rem;
        color: var(--text-soft) !important;
        max-width: 760px;
        line-height: 1.7;
    }

    .brand-pill-row {
        display: flex;
        gap: 0.7rem;
        flex-wrap: wrap;
        margin: 1rem 0 1.2rem 0;
    }

    .brand-pill {
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.86rem;
        border: 1px solid rgba(255,255,255,0.12);
        background: rgba(255,255,255,0.05);
        color: white !important;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0.25rem 0 1rem 0;
    }

    .glass-card {
        background: rgba(16, 22, 36, 0.76);
        border: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 1rem;
        box-shadow: var(--shadow-main);
    }

    .movie-card {
        background: linear-gradient(180deg, rgba(14, 20, 34, 0.95), rgba(8, 12, 22, 0.92));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 0.85rem;
        box-shadow: var(--shadow-main);
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
        margin-bottom: 1rem;
    }

    .movie-card:hover {
        transform: translateY(-6px);
        border-color: rgba(20,217,255,0.28);
        box-shadow: 0 18px 40px rgba(0,0,0,0.45);
    }

    .movie-title {
        font-size: 1rem;
        font-weight: 700;
        margin-top: 0.55rem;
        margin-bottom: 0.2rem;
    }

    .movie-meta {
        color: var(--text-soft) !important;
        font-size: 0.88rem;
        line-height: 1.55;
    }

    .platform-gradient-text {
        background: var(--grad-brand);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }

    .kpi-card {
        padding: 1rem 1rem 0.8rem 1rem;
        border-radius: 18px;
        background: var(--grad-card);
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: var(--shadow-main);
    }

    .kpi-label {
        color: var(--text-soft) !important;
        font-size: 0.86rem;
        margin-bottom: 0.35rem;
    }

    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: white !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.10);
        color: white;
        background: linear-gradient(90deg, #e50914, #00a8e1);
        font-weight: 700;
        padding: 0.72rem 1rem;
        box-shadow: 0 10px 24px rgba(0,0,0,0.25);
    }

    .stButton > button:hover {
        border-color: rgba(255,255,255,0.18);
        transform: translateY(-1px);
    }

    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stTextArea textarea {
        background: rgba(255,255,255,0.06) !important;
        color: white !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
    }

    div[data-testid="metric-container"] {
        background: linear-gradient(180deg, rgba(19, 27, 42, 0.96), rgba(10, 16, 28, 0.96));
        border: 1px solid rgba(255,255,255,0.08);
        padding: 1rem;
        border-radius: 18px;
        box-shadow: var(--shadow-main);
    }

    div[data-testid="metric-container"] label,
    div[data-testid="metric-container"] div {
        color: white !important;
    }

    .small-note {
        color: var(--text-soft) !important;
        font-size: 0.92rem;
    }

    .poster-img {
        border-radius: 16px;
        overflow: hidden;
    }

    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.15rem;
        }
        .hero-wrap {
            padding: 1.35rem;
            border-radius: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="padding:0.5rem 0 1rem 0;">
            <h2 style="margin:0;font-size:1.35rem;">🎬 OTT Stream Pro Max</h2>
            <p style="color:#aab6d3;margin-top:0.35rem;">
                Netflix + Prime + Hotstar inspired AI movie platform
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.info("Use the sidebar pages to browse, search, recommend, and manage your watchlist.")


def hero_section():
    st.markdown("""
    <div class="hero-wrap">
        <div class="brand-pill-row">
            <span class="brand-pill">NETFLIX VIBE</span>
            <span class="brand-pill">PRIME DEPTH</span>
            <span class="brand-pill">HOTSTAR ENERGY</span>
            <span class="brand-pill">AI RECOMMENDATIONS</span>
        </div>
        <div class="hero-title">
            One Screen for <span class="platform-gradient-text">Movies, Discovery, and AI Picks</span>
        </div>
        <div class="hero-sub">
            Premium dark OTT-style interface with intelligent recommendations, search,
            watchlist, analytics, and trailer-ready integrations.
        </div>
    </div>
    """, unsafe_allow_html=True)


def section_header(text):
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)


def movie_card(title, genre, overview):
    st.markdown(
        f"""
        <div class="movie-card">
            <div class="movie-title">{title}</div>
            <div class="movie-meta"><b>Genre:</b> {genre}</div>
            <div class="movie-meta" style="margin-top:0.35rem;">{overview}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def kpi_card(label, value):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
