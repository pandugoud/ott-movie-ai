import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --bg-1: #05070d;
        --bg-2: #0b1120;
        --bg-3: #111a2e;
        --glass: rgba(16, 22, 36, 0.74);
        --glass-2: rgba(7, 12, 22, 0.88);
        --text: #f5f7ff;
        --muted: #98a8c7;
        --border: rgba(255,255,255,0.09);
        --netflix: #e50914;
        --prime: #00a8e1;
        --hotstar: #14d9ff;
        --gold: #ffd166;
        --shadow: 0 14px 35px rgba(0,0,0,0.35);
        --glow: 0 0 0 1px rgba(20,217,255,0.20), 0 20px 40px rgba(0,0,0,0.45);
        --brand: linear-gradient(90deg, #e50914 0%, #00a8e1 55%, #14d9ff 100%);
        --brand-soft: linear-gradient(135deg, rgba(229,9,20,0.22), rgba(10,15,28,0.88) 45%, rgba(0,168,225,0.18) 75%, rgba(20,217,255,0.12));
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(229,9,20,0.16), transparent 22%),
            radial-gradient(circle at 95% 5%, rgba(0,168,225,0.14), transparent 24%),
            radial-gradient(circle at 50% 100%, rgba(20,217,255,0.07), transparent 18%),
            linear-gradient(180deg, #04060b 0%, #07101c 42%, #091423 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(4, 7, 12, 0.65);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(5,8,15,0.98), rgba(8,14,26,0.98));
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] * {
        color: #eef3ff !important;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, h4, h5, p, span, label, div {
        color: var(--text);
    }

    .topbar {
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding: 0.4rem 0 1rem 0;
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

    .hero-shell {
        position: relative;
        overflow: hidden;
        min-height: 540px;
        border-radius: 30px;
        background: var(--brand-soft);
        border: 1px solid var(--border);
        box-shadow: var(--shadow);
        padding: 2rem;
        margin-bottom: 1.25rem;
    }

    .hero-grid {
        display: grid;
        grid-template-columns: 1.1fr 0.9fr;
        gap: 1.25rem;
        align-items: end;
        min-height: 480px;
    }

    .hero-pill-row {
        display: flex;
        gap: 0.75rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }

    .hero-pill {
        padding: 0.46rem 0.9rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.10);
        font-size: 0.82rem;
        font-weight: 800;
        backdrop-filter: blur(10px);
    }

    .hero-title {
        font-size: 4rem;
        line-height: 0.98;
        font-weight: 900;
        letter-spacing: -0.055em;
        max-width: 700px;
        margin-bottom: 0.8rem;
    }

    .hero-title .accent {
        background: var(--brand);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-desc {
        max-width: 700px;
        font-size: 1.03rem;
        color: var(--muted) !important;
        line-height: 1.8;
        margin-bottom: 1.2rem;
    }

    .hero-meta-row {
        display: flex;
        gap: 0.7rem;
        flex-wrap: wrap;
        margin-bottom: 1.4rem;
    }

    .meta-chip {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 999px;
        padding: 0.5rem 0.9rem;
        font-size: 0.86rem;
        color: #e9f0ff !important;
    }

    .hero-actions {
        display: flex;
        gap: 0.85rem;
        flex-wrap: wrap;
    }

    .cta-row {
        margin-top: 1rem;
    }

    .hero-poster-card {
        align-self: stretch;
        display:flex;
        flex-direction:column;
        justify-content:flex-end;
        border-radius: 26px;
        background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        padding: 1rem;
        box-shadow: var(--glow);
    }

    .section-title {
        font-size: 1.22rem;
        font-weight: 800;
        margin: 0.4rem 0 1rem 0;
        letter-spacing: -0.02em;
    }

    .section-sub {
        color: var(--muted) !important;
        margin-top: -0.4rem;
        margin-bottom: 0.9rem;
        font-size: 0.94rem;
    }

    .rail-wrap {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 24px;
        padding: 1rem;
        margin-bottom: 1.15rem;
        box-shadow: var(--shadow);
    }

    .poster-card {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        background: linear-gradient(180deg, rgba(15,20,34,0.96), rgba(8,12,20,0.96));
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: var(--shadow);
        padding: 0.55rem;
        transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }

    .poster-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--glow);
        border-color: rgba(20,217,255,0.24);
    }

    .poster-meta {
        padding: 0.65rem 0.2rem 0.25rem 0.2rem;
    }

    .poster-title {
        font-size: 0.98rem;
        font-weight: 800;
        line-height: 1.25;
        margin-bottom: 0.25rem;
    }

    .poster-sub {
        color: var(--muted) !important;
        font-size: 0.86rem;
    }

    .detail-card {
        background: linear-gradient(180deg, rgba(15,20,34,0.96), rgba(8,12,20,0.96));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 1rem;
        box-shadow: var(--shadow);
    }

    .overview-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 1rem;
    }

    .metric-chip-grid {
        display:grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.8rem;
        margin-bottom: 1rem;
    }

    .metric-chip {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 18px;
        padding: 0.9rem;
    }

    .metric-chip .label {
        color: var(--muted) !important;
        font-size: 0.84rem;
        margin-bottom: 0.2rem;
    }

    .metric-chip .value {
        font-size: 1.15rem;
        font-weight: 800;
    }

    .glass-card {
        background: var(--glass);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 22px;
        padding: 1rem;
        box-shadow: var(--shadow);
    }

    .mini-note {
        color: var(--muted) !important;
        font-size: 0.92rem;
    }

    .stButton > button {
        width: 100%;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.10);
        color: white;
        font-weight: 800;
        padding: 0.82rem 1rem;
        background: linear-gradient(90deg, #e50914, #00a8e1);
        box-shadow: 0 12px 26px rgba(0,0,0,0.24);
    }

    .stButton > button:hover {
        border-color: rgba(255,255,255,0.18);
    }

    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] > div,
    .stTextArea textarea {
        background: rgba(255,255,255,0.06) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 15px !important;
    }

    div[data-testid="metric-container"] {
        background: linear-gradient(180deg, rgba(15,20,34,0.96), rgba(9,13,22,0.96));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: var(--shadow);
    }

    div[data-testid="stDialog"] div[role="dialog"] {
        border-radius: 28px !important;
        background: linear-gradient(180deg, rgba(5,8,15,0.98), rgba(10,16,28,0.98)) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        box-shadow: 0 30px 70px rgba(0,0,0,0.45) !important;
    }

    .cinema-dialog-anchor { display:none; }

    @media (max-width: 980px) {
        .hero-grid {
            grid-template-columns: 1fr;
        }
        .hero-title {
            font-size: 2.8rem;
        }
        .hero-shell {
            min-height: auto;
        }
    }

    @media (max-width: 640px) {
        .hero-title {
            font-size: 2.2rem;
        }
        .hero-shell {
            padding: 1.2rem;
            border-radius: 24px;
        }
        .metric-chip-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="padding:0.35rem 0 0.9rem 0;">
            <div style="font-size:1.25rem;font-weight:900;">🎬 OTT Stream Pro Max</div>
            <div style="color:#98a8c7;margin-top:0.35rem;">
                Premium movie discovery UI with cinematic trailer experience
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.info("Home lo featured banner, popup trailer, and full player page ni use cheyyandi.")


def topbar():
    st.markdown("""
    <div class="topbar">
        <div class="brand-logo"><span>OTT Stream Pro Max</span></div>
        <div class="mini-note">Netflix + Prime + Hotstar inspired premium dark UI</div>
    </div>
    """, unsafe_allow_html=True)


def section_header(title, sub=None):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<div class="section-sub">{sub}</div>', unsafe_allow_html=True)


def movie_card(title, genre, overview):
    st.markdown(f"""
    <div class="detail-card">
        <div style="font-size:1.05rem;font-weight:800;margin-bottom:0.3rem;">{title}</div>
        <div class="mini-note" style="margin-bottom:0.45rem;"><b>Genre:</b> {genre}</div>
        <div class="mini-note">{overview}</div>
    </div>
    """, unsafe_allow_html=True)
