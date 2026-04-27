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
        padding-bottom: 
