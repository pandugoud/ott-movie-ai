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
        --top-safe-space: 4.2rem;
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
        position: sticky;
        top: 0;
        z-index: 999;
        background: rgba(6, 16, 24, 0.82);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(255,255,255,0.04);
        min-height: 3rem;
    }

    [data-testid="stToolbar"] {
        top: 0.2rem;
        right: 0.6rem;
    }

    .block-container {
        max-width: 1400px;
        padding-top: calc(var(--top-safe-space) + 0.8rem) !important;
        padding-bottom: 1.5rem;
    }

    .stMainBlockContainer {
        padding-top: calc(var(--top-safe-space) + 0.8rem) !important;
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
        margin-bottom: 1rem;
        padding-top: 0.2rem;
        padding-bottom: 0.35rem;
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
        margin-top: 0.25rem;
        margin-bottom: 1rem;
    }

    @media (max-width: 640px) {
        :root {
            --top-safe-space: 4.8rem;
        }

        .block-container {
            padding-top: calc(var(--top-safe-space) + 0.6rem) !important;
            padding-bottom: 1rem;
        }

        .stMainBlockContainer {
            padding-top: calc(var(--top-safe-space) + 0.6rem) !important;
        }

        .topbar {
            flex-direction: column;
            align-items: flex-start;
            margin-bottom: 0.8rem;
        }

        .hero-v2 {
            margin-top: 0.15rem;
            padding: 1.05rem;
            border-radius: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
