import streamlit as st
from src.recommender import load_data, get_genre_counts
from src.ui import inject_css, render_sidebar, section_header
from src.utils import initialize_session

st.set_page_config(page_title="Analytics | OTT Stream Pro Max", page_icon="📊", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("📊 Analytics Dashboard")

df = load_data()
genre_counts = get_genre_counts()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Movies", len(df))
with col2:
    st.metric("Genres", df["genre"].nunique())
with col3:
    st.metric("Watchlist Items", len(st.session_state.watchlist))

section_header("Genre Distribution")
st.bar_chart(genre_counts)

section_header("Session Overview")
st.markdown(f"""
<div class="glass-card">
    <p><b>Total catalog:</b> {len(df)} movies</p>
    <p><b>Top genre:</b> {genre_counts.index[0] if not genre_counts.empty else 'N/A'}</p>
    <p><b>Saved in watchlist:</b> {len(st.session_state.watchlist)}</p>
</div>
""", unsafe_allow_html=True)
