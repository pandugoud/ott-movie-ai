import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --text: #f5f7ff;
        --muted: #9aa8c3;
        --line: rgba(255,255,255,0.08);
        --red: #e50914;
        --blue: #00a8e1;
        --cyan: #14d9ff;
        --gold: #ffd166;
        --brand: linear-gradient(90deg, #e50914 0%, #00a8e1 50%, #14d9ff 100%);
        --hero-bg:
            radial-gradient(circle at 0% 0%, rgba(229,9,20,0.18), transparent 24%),
            radial-gradient(circle at 100% 0%, rgba(20,217,255,0.15), transparent 24%),
            linear-gradient(135deg, rgba(13,18,32,0.98), rgba(8,13,23,0.96));
        --shadow: 0 18px 38px rgba(0,0,0,0.34);
        --shadow-2: 0 10px 24px rgba(0,0,0,0.30);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 15% 0%, rgba(229,9,20,0.10), transparent 22%),
            radial-gradient(circle at 90% 5%, rgba(20,217,255,0.08), transparent 20%),
            linear-gradient(180deg, #03050a 0%, #08101d 46%, #091522 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(4, 7, 12, 0.6);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(4,6,12,0.98), rgba(8,13,24,0.98));
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] * {
        color: #eef3ff !important;
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
    }

    .brand-logo span {
        background: var(--brand);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .compact-note {
        color: var(--muted);
        font-size: 0.92rem;
    }

    .hero-v2 {
        border-radius: 30px;
        padding: 1.35rem;
        background: var(--hero-bg);
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
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
        font-size: 0.74rem;
        font-weight: 800;
    }

    .hero-title {
        font-size: 3.3rem;
        line-height: 0.98;
        font-weight: 900;
        letter-spacing: -0.06em;
        margin-bottom: 0.75rem;
    }

    .hero-title .accent {
        background: var(--brand);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
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
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        font-size: 0.84rem;
    }

    .hero-poster-box {
        background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 0.85rem;
        box-shadow: var(--shadow-2);
        height: 100%;
    }

    .section-title {
        font-size: 1.16rem;
        font-weight: 800;
        margin: 1rem 0 0.25rem 0;
        letter-spacing: -0.02em;
    }

    .section-sub {
        color: var(--muted) !important;
        margin-bottom: 0.9rem;
        font-size: 0.92rem;
    }

    .rail-card {
        background: linear-gradient(180deg, rgba(12,18,31,0.94), rgba(8,12,22,0.96));
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 24px;
        padding: 1rem;
        margin-bottom: 1.1rem;
        box-shadow: var(--shadow-2);
    }

    .grid-card {
        background: linear-gradient(180deg, rgba(13,18,31,0.96), rgba(8,12,22,0.96));
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 22px;
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
    }

    .movie-sub {
        color: var(--muted) !important;
        font-size: 0.83rem;
        margin-top: 0.18rem;
        margin-bottom: 0.65rem;
    }

    .mini-stat {
        color: var(--gold) !important;
        font-weight: 700;
    }

    .watch-chip {
        display:inline-block;
        padding:0.36rem 0.7rem;
        border-radius:999px;
        background:rgba(255,255,255,0.06);
        border:1px solid rgba(255,255,255,0.08);
        font-size:0.78rem;
        margin-right:0.4rem;
        margin-bottom:0.4rem;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.08);
        color: white;
        font-weight: 800;
        padding: 0.74rem 0.95rem;
        background: linear-gradient(90deg, #e50914, #00a8e1);
        box-shadow: 0 10px 20px rgba(0,0,0,0.24);
        font-size: 0.9rem;
    }

    div[data-testid="stDialog"] div[role="dialog"] {
        border-radius: 28px !important;
        background: linear-gradient(180deg, rgba(5,8,15,0.98), rgba(10,16,28,0.98)) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        box-shadow: 0 30px 70px rgba(0,0,0,0.45) !important;
    }

    @media (max-width: 980px) {
        .hero-title {
            font-size: 2.6rem;
        }
    }

    @media (max-width: 640px) {
        .hero-title {
            font-size: 2.1rem;
        }
        .hero-v2 {
            padding: 1rem;
            border-radius: 24px;
        }
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
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="padding:0.35rem 0 0.9rem 0;">
            <div style="font-size:1.2rem;font-weight:900;">🎬 OTT Stream Pro Max</div>
            <div style="color:#98a8c7;margin-top:0.35rem;">
                Premium movie discovery UI with cinematic trailer experience
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.info("Home v2 lo compact hero, clean poster cards, and popup trailer untayi.")


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
        <div style="color:#9aa8c3; font-size:0.9rem; line-height:1.6;">
            {overview}
        </div>
    </div>
    """, unsafe_allow_html=True)
