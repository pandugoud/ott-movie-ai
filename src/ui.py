import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg-main: #07111f;
        --text-main: #f4f7ff;
        --text-soft: #9fb0d0;
        --card-bg: rgba(16, 22, 36, 0.82);
        --card-bg-2: rgba(10, 16, 28, 0.92);
        --border-soft: rgba(255,255,255,0.08);
        --netflix: #e50914;
        --prime: #00a8e1;
        --hotstar: #14d9ff;
        --shadow: 0 16px 35px rgba(0,0,0,0.35);
        --brand-grad: linear-gradient(90deg, #e50914 0%, #00a8e1 55%, #14d9ff 100%);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(229,9,20,0.16), transparent 24%),
            radial-gradient(circle at top right, rgba(0,168,225,0.16), transparent 28%),
            radial-gradient(circle at bottom center, rgba(20,217,255,0.08), transparent 18%),
            linear-gradient(180deg, #05070d 0%, #08111d 45%, #091423 100%);
        color: var(--text-main);
    }

    [data-testid="stHeader"] {
        background: rgba(4, 8, 14, 0.72);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(5,8,15,0.98) 0%, rgba(8,14,26,0.98) 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] * {
        color: #eff4ff !important;
    }

    .block-container {
        max-width: 1360px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: var(--text-main);
    }

    .hero-wrap {
        padding: 2.3rem 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(229,9,20,0.20), rgba(7,12,22,0.88) 40%, rgba(0,168,225,0.18) 72%, rgba(20,217,255,0.14));
        border: 1px solid var(--border-soft);
        box-shadow: var(--shadow);
        margin-bottom: 1.2rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.04;
        letter-spacing: -0.03em;
        margin-bottom: 0.6rem;
    }

    .hero-sub {
        font-size: 1.03rem;
        color: var(--text-soft) !important;
        max-width: 720px;
        line-height: 1.75;
    }

    .pill-row {
        display: flex;
        gap: 0.7rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }

    .pill {
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 800;
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
    }

    .gradient-text {
        background: var(--brand-grad);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .glass-card {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 1rem;
        box-shadow: var(--shadow);
    }

    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin: 0.4rem 0 1rem 0;
    }

    .movie-card {
        background: linear-gradient(180deg, rgba(15, 20, 34, 0.96), rgba(8, 12, 20, 0.96));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 0.9rem;
        box-shadow: var(--shadow);
        margin-top: 0.5rem;
        margin-bottom: 0.9rem;
    }

    .movie-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }

    .movie-meta {
        color: var(--text-soft) !important;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .video-frame {
        background: rgba(4, 8, 15, 0.96);
        border-radius: 18px;
        padding: 0.35rem;
        border: 1px solid rgba(20,217,255,0.18);
        box-shadow: var(--shadow);
        margin-bottom: 0.6rem;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.10);
        color: white;
        font-weight: 700;
        padding: 0.75rem 1rem;
        background: linear-gradient(90deg, #e50914, #00a8e1);
        box-shadow: 0 12px 26px rgba(0,0,0,0.24);
    }

    .stButton > button:hover {
        border-color: rgba(255,255,255,0.18);
    }

    .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.06) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 14px !important;
    }

    div[data-testid="metric-container"] {
        background: linear-gradient(180deg, rgba(15,20,34,0.96), rgba(9,13,22,0.96));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: var(--shadow);
    }

    .small-note {
        color: var(--text-soft) !important;
        font-size: 0.92rem;
    }

    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.1rem;
        }
        .hero-wrap {
            padding: 1.4rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="padding-top:0.4rem;padding-bottom:0.8rem;">
            <h2 style="margin:0;">🎬 OTT Stream Pro Max</h2>
            <p style="color:#9fb0d0;margin-top:0.35rem;">
                Netflix + Prime + Hotstar style dark AI movie platform
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.info("Sidebar lo pages open chesi browse cheyyandi.")


def hero_section():
    st.markdown("""
    <div class="hero-wrap">
        <div class="pill-row">
            <span class="pill">NETFLIX</span>
            <span class="pill">PRIME VIDEO</span>
            <span class="pill">HOTSTAR</span>
            <span class="pill">AI RECOMMENDER</span>
            <span class="pill">CLICK TO PLAY</span>
        </div>
        <div class="hero-title">
            Premium <span class="gradient-text">OTT Experience</span> with Posters, Trailers, and Smart Picks
        </div>
        <div class="hero-sub">
            Posters ni click chesi trailer play cheyyachu, play button meeda click chesi kuda same place lo video start avvachu.
        </div>
    </div>
    """, unsafe_allow_html=True)


def section_header(text):
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)


def movie_card(title, genre, overview):
    st.markdown(f"""
    <div class="movie-card">
        <div class="movie-title">{title}</div>
        <div class="movie-meta"><b>Genre:</b> {genre}</div>
        <div class="movie-meta" style="margin-top:0.35rem;">{overview}</div>
    </div>
    """, unsafe_allow_html=True)
