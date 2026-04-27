import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --bg: #061018;
        --bg-2: #091722;
        --panel: rgba(10, 22, 34, 0.78);
        --card: rgba(14, 30, 46, 0.92);
        --card-2: rgba(11, 25, 38, 0.96);
        --text: #edf2f7;
        --muted: #91a4b7;
        --line: rgba(255,255,255,0.08);
        --line-strong: rgba(255,255,255,0.14);
        --primary: #14b8a6;
        --primary-hover: #0ea392;
        --accent: #f59e0b;
        --shadow-sm: 0 10px 24px rgba(0,0,0,0.18);
        --shadow-md: 0 20px 48px rgba(0,0,0,0.28);
        --shadow-lg: 0 28px 80px rgba(0,0,0,0.36);
         --top-safe-space: 7.8rem;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(20,184,166,0.12), transparent 26%),
            radial-gradient(circle at top right, rgba(245,158,11,0.08), transparent 18%),
            linear-gradient(180deg, #061018 0%, #09131d 50%, #061018 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(6, 16, 24, 0.58);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(255,255,255,0.04);
        height: 2.6rem;
    }

    [data-testid="stToolbar"] {
        top: 0.15rem;
        right: 0.6rem;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 0.9rem;
        padding-bottom: 1.5rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10,20,32,0.98) 0%, rgba(8,17,27,0.98) 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] * {
        color: var(--text) !important;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        margin-bottom: 0.85rem;
        padding: 0.1rem 0 0.3rem 0;
    }

    .brand-wrap {
        display:flex;
        align-items:center;
        gap:0.85rem;
    }

    .brand-mark {
        width: 46px;
        height: 46px;
        border-radius: 15px;
        display:flex;
        align-items:center;
        justify-content:center;
        background: linear-gradient(135deg, rgba(20,184,166,0.22), rgba(20,184,166,0.08));
        border: 1px solid rgba(20,184,166,0.20);
        box-shadow: var(--shadow-sm);
        font-size: 1.15rem;
    }

    .brand-logo {
        font-size: 1.35rem;
        font-weight: 900;
        line-height: 1;
        letter-spacing: -0.04em;
        color: var(--text);
    }

    .brand-logo span {
        color: var(--primary);
    }

    .brand-sub {
        color: var(--muted);
        font-size: 0.88rem;
        margin-top: 0.22rem;
    }

    .compact-note {
        color: var(--muted);
        font-size: 0.88rem;
        padding: 0.62rem 0.92rem;
        border-radius: 999px;
        border: 1px solid var(--line);
        background: rgba(255,255,255,0.03);
    }

    .hero-v2 {
        position: relative;
        overflow: hidden;
        border-radius: 26px;
        padding: 1.35rem;
        background:
            linear-gradient(135deg, rgba(20,184,166,0.10), rgba(255,255,255,0.02)),
            rgba(10, 22, 34, 0.78);
        border: 1px solid var(--line);
        backdrop-filter: blur(12px);
        box-shadow: var(--shadow-md);
        margin-bottom: 1rem;
    }

    .hero-v2::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(circle at 82% 20%, rgba(20,184,166,0.12), transparent 20%),
            radial-gradient(circle at 18% 80%, rgba(245,158,11,0.08), transparent 18%);
        pointer-events: none;
    }

    .hero-pills, .hero-title, .hero-desc, .hero-meta {
        position: relative;
        z-index: 1;
    }

    .hero-pills {
        display:flex;
        gap:0.55rem;
        flex-wrap:wrap;
        margin-bottom: 0.95rem;
    }

    .hero-pill {
        padding: 0.42rem 0.78rem;
        border-radius: 999px;
        background: rgba(20,184,166,0.10);
        border: 1px solid rgba(20,184,166,0.22);
        color: #d8fffa;
        font-size: 0.73rem;
        font-weight: 800;
        letter-spacing: 0.03em;
    }

    .hero-title {
        font-size: 3rem;
        line-height: 1.02;
        font-weight: 900;
        letter-spacing: -0.05em;
        margin-bottom: 0.7rem;
        color: var(--text);
        max-width: 12ch;
    }

    .hero-title .accent {
        color: var(--primary);
    }

    .hero-desc {
        font-size: 0.98rem;
        line-height: 1.8;
        color: var(--muted) !important;
        max-width: 68ch;
        margin-bottom: 1rem;
    }

    .hero-meta {
        display:flex;
        flex-wrap:wrap;
        gap:0.55rem;
    }

    .meta-chip {
        padding: 0.45rem 0.76rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        font-size: 0.83rem;
        color: var(--text);
    }

    .hero-poster-box,
    .grid-card,
    .stat-card,
    .panel-card {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
            var(--card);
        border: 1px solid var(--line);
        box-shadow: var(--shadow-sm);
    }

    .hero-poster-box {
        border-radius: 24px;
        padding: 0.95rem;
        height: 100%;
    }

    .grid-card {
        border-radius: 20px;
        padding: 0.9rem;
        margin-bottom: 0.8rem;
        transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
    }

    .grid-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-md);
        border-color: rgba(20,184,166,0.22);
    }

    .panel-card {
        border-radius: 20px;
        padding: 1rem;
        margin-bottom: 0.9rem;
    }

    .section-title {
        font-size: 1.16rem;
        font-weight: 800;
        margin: 0.9rem 0 0.22rem 0;
        letter-spacing: -0.02em;
        color: var(--text);
    }

    .section-sub {
        color: var(--muted) !important;
        margin-bottom: 0.85rem;
        font-size: 0.92rem;
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
        margin-top: 0.18rem;
        margin-bottom: 0.65rem;
    }

    .mini-stat {
        color: var(--accent) !important;
        font-weight: 800;
    }

    .stat-card {
        border-radius: 18px;
        padding: 1rem;
    }

    .stat-label {
        color: var(--muted);
        font-size: 0.82rem;
        margin-bottom: 0.35rem;
    }

    .stat-value {
        color: var(--text);
        font-size: 1.55rem;
        font-weight: 900;
        letter-spacing: -0.04em;
    }

    .glass-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.10), transparent);
        margin: 0.95rem 0 1rem;
    }

    .poster-box {
        width: 100%;
        height: 320px;
        border-radius: 16px;
        overflow: hidden;
        background: #0b1520;
        border: 1px solid rgba(255,255,255,0.05);
    }

    .poster-box.poster-lg {
        height: 470px;
        border-radius: 18px;
    }

    .poster-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
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
        background: linear-gradient(180deg, #14b8a6 0%, #0ea392 100%);
        box-shadow: 0 10px 20px rgba(20,184,166,0.14);
        font-size: 0.88rem;
        white-space: nowrap;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        background: linear-gradient(180deg, #1bc8b6 0%, #11a897 100%);
        border-color: rgba(20,184,166,0.32);
        color: #ffffff;
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
        gap: 0.45rem;
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

    .sidebar-brand {
        padding: 0.2rem 0 1rem 0;
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
        margin-top: 0.8rem;
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
            font-size: 2.35rem;
            max-width: 100%;
        }

        .poster-box.poster-lg {
            height: 380px;
        }
    }

    @media (max-width: 640px) {
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 1rem;
        }

        .topbar {
            flex-direction: column;
            align-items: flex-start;
        }

        .compact-note {
            width: 100%;
        }

        .hero-v2 {
            padding: 1.05rem;
            border-radius: 20px;
        }

        .hero-title {
            font-size: 2rem;
        }

        .poster-box {
            height: 260px;
        }

        .poster-box.poster-lg {
            height: 320px;
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
                Rich OTT-inspired movie platform with mood AI, watchlist, trailers, analytics, and premium layouts.
            </div>
            <div class="sidebar-chip-wrap">
                <span class="sidebar-chip">Premium UI</span>
                <span class="sidebar-chip">Mood AI</span>
                <span class="sidebar-chip">Trailers</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def topbar():
    st.markdown("""
    <div class="topbar">
        <div class="brand-wrap">
            <div class="brand-mark">🎥</div>
            <div>
                <div class="brand-logo"><span>OTT Stream</span> Pro Max</div>
                <div class="brand-sub">Smarter discovery • Richer design • Better browsing</div>
            </div>
        </div>
        <div class="compact-note">Premium dark experience</div>
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


def panel_card_start():
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)


def panel_card_end():
    st.markdown('</div>', unsafe_allow_html=True)


def poster_image(url, large=False):
    box_class = "poster-box poster-lg" if large else "poster-box"
    st.markdown(f'''
        <div class="{box_class}">
            <img src="{url}" alt="movie poster">
        </div>
    ''', unsafe_allow_html=True)
