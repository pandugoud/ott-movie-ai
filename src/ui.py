import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --bg: #07111b;
        --bg-soft: #0d1b2a;
        --panel: rgba(13, 27, 42, 0.72);
        --panel-strong: #102235;
        --card: rgba(16, 34, 53, 0.88);
        --card-2: rgba(13, 31, 48, 0.95);
        --text: #edf2f7;
        --muted: #94a3b8;
        --line: rgba(255,255,255,0.08);
        --line-strong: rgba(255,255,255,0.14);
        --primary: #14b8a6;
        --primary-hover: #0f9e8f;
        --accent: #f59e0b;
        --danger: #ef4444;
        --shadow-sm: 0 10px 24px rgba(0,0,0,0.18);
        --shadow-md: 0 18px 42px rgba(0,0,0,0.28);
        --shadow-lg: 0 30px 70px rgba(0,0,0,0.34);
        --blur: blur(14px);
        --radius-xl: 24px;
        --radius-lg: 18px;
        --radius-md: 14px;
        --radius-sm: 12px;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(20,184,166,0.10), transparent 28%),
            radial-gradient(circle at top right, rgba(245,158,11,0.08), transparent 22%),
            linear-gradient(180deg, #07111b 0%, #08131f 45%, #07111b 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(7,17,27,0.72);
        backdrop-filter: blur(16px);
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stToolbar"] {
        right: 1rem;
    }

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, rgba(13,27,42,0.96) 0%, rgba(10,20,32,0.96) 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] * {
        color: var(--text) !important;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.1rem;
        padding: 0.2rem 0 0.7rem 0;
    }

    .brand-wrap {
        display:flex;
        align-items:center;
        gap:0.85rem;
    }

    .brand-badge {
        width: 44px;
        height: 44px;
        border-radius: 14px;
        display:flex;
        align-items:center;
        justify-content:center;
        background: linear-gradient(135deg, rgba(20,184,166,0.22), rgba(20,184,166,0.08));
        border: 1px solid rgba(20,184,166,0.24);
        box-shadow: var(--shadow-sm);
        font-size: 1.2rem;
    }

    .brand-logo {
        font-size: 1.35rem;
        font-weight: 900;
        letter-spacing: -0.04em;
        line-height: 1;
        color: var(--text);
    }

    .brand-logo span {
        color: var(--primary);
    }

    .brand-sub {
        color: var(--muted);
        font-size: 0.88rem;
        margin-top: 0.2rem;
    }

    .compact-note {
        color: var(--muted);
        font-size: 0.9rem;
        padding: 0.65rem 0.95rem;
        border-radius: 999px;
        border: 1px solid var(--line);
        background: rgba(255,255,255,0.03);
    }

    .hero-v2 {
        position: relative;
        overflow: hidden;
        border-radius: var(--radius-xl);
        padding: 1.5rem;
        background:
            linear-gradient(135deg, rgba(20,184,166,0.10), rgba(255,255,255,0.02)),
            rgba(13, 27, 42, 0.78);
        border: 1px solid var(--line);
        backdrop-filter: var(--blur);
        box-shadow: var(--shadow-md);
        margin-bottom: 1.15rem;
    }

    .hero-v2::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(circle at 85% 18%, rgba(20,184,166,0.14), transparent 20%),
            radial-gradient(circle at 15% 85%, rgba(245,158,11,0.10), transparent 18%);
        pointer-events: none;
    }

    .hero-pills {
        display:flex;
        gap:0.55rem;
        flex-wrap:wrap;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }

    .hero-pill {
        padding: 0.45rem 0.82rem;
        border-radius: 999px;
        background: rgba(20,184,166,0.10);
        border: 1px solid rgba(20,184,166,0.24);
        font-size: 0.74rem;
        font-weight: 800;
        color: #d9fffa;
        letter-spacing: 0.03em;
    }

    .hero-title {
        position: relative;
        z-index: 1;
        font-size: 3.25rem;
        line-height: 1.02;
        font-weight: 900;
        letter-spacing: -0.05em;
        margin-bottom: 0.78rem;
        color: var(--text);
        max-width: 12ch;
    }

    .hero-title .accent {
        color: var(--primary);
    }

    .hero-desc {
        position: relative;
        z-index: 1;
        font-size: 1rem;
        line-height: 1.85;
        color: var(--muted) !important;
        margin-bottom: 1rem;
        max-width: 70ch;
    }

    .hero-meta {
        display:flex;
        gap:0.6rem;
        flex-wrap:wrap;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }

    .meta-chip {
        padding: 0.46rem 0.78rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        font-size: 0.84rem;
        color: var(--text);
    }

    .section-title {
        font-size: 1.18rem;
        font-weight: 800;
        margin: 1rem 0 0.22rem 0;
        letter-spacing: -0.02em;
        color: var(--text);
    }

    .section-sub {
        color: var(--muted) !important;
        margin-bottom: 0.9rem;
        font-size: 0.92rem;
    }

    .grid-card {
        position: relative;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%),
            var(--card-2);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 0.9rem;
        box-shadow: var(--shadow-sm);
        overflow: hidden;
        margin-bottom: 0.8rem;
        transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
    }

    .grid-card:hover {
        transform: translateY(-4px);
        border-color: rgba(20,184,166,0.22);
        box-shadow: var(--shadow-md);
    }

    .poster-frame img {
        border-radius: 14px !important;
    }

    .movie-title {
        font-size: 1rem;
        font-weight: 800;
        margin-top: 0.15rem;
        line-height: 1.28;
        color: var(--text);
    }

    .movie-sub {
        color: var(--muted) !important;
        font-size: 0.83rem;
        margin-top: 0.2rem;
        margin-bottom: 0.65rem;
    }

    .mini-stat {
        color: var(--accent) !important;
        font-weight: 800;
    }

    .hero-poster-box {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
            var(--card);
        border: 1px solid var(--line);
        border-radius: 22px;
        padding: 0.9rem;
        box-shadow: var(--shadow-md);
        height: 100%;
    }

    .stat-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: var(--shadow-sm);
    }

    .stat-label {
        color: var(--muted);
        font-size: 0.84rem;
        margin-bottom: 0.4rem;
    }

    .stat-value {
        color: var(--text);
        font-size: 1.55rem;
        font-weight: 900;
        letter-spacing: -0.03em;
    }

    .glass-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.10), transparent);
        margin: 1rem 0;
    }

    .stButton > button {
        width: 100%;
        min-height: 44px;
        height: 44px;
        border-radius: 12px;
        border: 1px solid rgba(20,184,166,0.20);
        color: #ffffff;
        font-weight: 700;
        padding: 0.65rem 0.95rem;
        background: linear-gradient(180deg, #14b8a6 0%, #0f9e8f 100%);
        box-shadow: 0 10px 22px rgba(20,184,166,0.14);
        font-size: 0.88rem;
        transition: all 0.2s ease;
        white-space: nowrap;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        background: linear-gradient(180deg, #19c7b5 0%, #0ea392 100%);
        border-color: rgba(20,184,166,0.34);
        color: #ffffff;
    }

    .stButton > button:focus {
        color: #ffffff;
        box-shadow: 0 0 0 0.18rem rgba(20,184,166,0.18);
    }

    .stTextInput input,
    .stTextArea textarea,
    div[data-baseweb="select"] > div,
    div[data-baseweb="base-input"] {
        background: rgba(255,255,255,0.03) !important;
        color: var(--text) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.4rem;
        background: rgba(255,255,255,0.03);
        padding: 0.4rem;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        height: 44px;
        padding: 0 1rem;
        color: var(--muted);
    }

    .stTabs [aria-selected="true"] {
        background: rgba(20,184,166,0.12) !important;
        color: var(--text) !important;
    }

    [data-testid="stMetric"] {
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--line);
        padding: 1rem;
        border-radius: 18px;
        box-shadow: var(--shadow-sm);
    }

    div[data-testid="stImage"] img {
        border-radius: 16px;
    }

    .sidebar-brand {
        padding: 0.3rem 0 1rem 0;
    }

    .sidebar-title {
        font-size: 1.16rem;
        font-weight: 900;
        color: var(--text);
    }

    .sidebar-sub {
        color: var(--muted);
        margin-top: 0.35rem;
        line-height: 1.6;
        font-size: 0.9rem;
    }

    .sidebar-chip-wrap {
        display:flex;
        gap:0.45rem;
        flex-wrap:wrap;
        margin-top: 0.85rem;
    }

    .sidebar-chip {
        padding: 0.34rem 0.6rem;
        border-radius: 999px;
        font-size: 0.72rem;
        background: rgba(20,184,166,0.10);
        border: 1px solid rgba(20,184,166,0.18);
        color: #d9fffa;
        font-weight: 700;
    }

    @media (max-width: 900px) {
        .hero-title {
            font-size: 2.45rem;
            max-width: 100%;
        }
    }

    @media (max-width: 640px) {
        .topbar {
            flex-direction: column;
            align-items: flex-start;
        }

        .compact-note {
            width: 100%;
        }

        .block-container {
            padding-top: 1.35rem;
            padding-bottom: 1.4rem;
        }

        .hero-v2 {
            padding: 1.1rem;
            border-radius: 20px;
        }

        .hero-title {
            font-size: 2rem;
        }

        .stButton > button {
            min-height: 42px;
            height: 42px;
            font-size: 0.82rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-brand">
            <div class="sidebar-title">🎬 OTT Stream Pro Max</div>
            <div class="sidebar-sub">
                Premium movie discovery experience with mood AI, trailer view, watchlist, and cleaner OTT-inspired design.
            </div>
            <div class="sidebar-chip-wrap">
                <span class="sidebar-chip">Mood AI</span>
                <span class="sidebar-chip">Watchlist</span>
                <span class="sidebar-chip">Trailers</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def topbar():
    st.markdown("""
    <div class="topbar">
        <div class="brand-wrap">
            <div class="brand-badge">🎥</div>
            <div>
                <div class="brand-logo"><span>OTT Stream</span> Pro Max</div>
                <div class="brand-sub">Smarter discovery. Better browsing. Cleaner OTT feel.</div>
            </div>
        </div>
        <div class="compact-note">Premium dark experience • AI-powered movie discovery</div>
    </div>
    """, unsafe_allow_html=True)


def section_header(title, sub=None):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<div class="section-sub">{sub}</div>', unsafe_allow_html=True)


def stat_card(label, value):
    st.markdown(f'''
    <div class="stat-card">
        <div class="stat-label">{label}</div>
        <div class="stat-value">{value}</div>
    </div>
    ''', unsafe_allow_html=True)
