import streamlit as st
from src.recommender import load_data, get_genre_counts
from src.ui import inject_css, render_sidebar, section_header, kpi_card
from src.utils import initialize_session

st.set_page_config(page_title="Analytics | OTT Stream Pro Max", page_icon="📊", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("📊 Analytics Dashboard")

df = load_data()
genre_counts = get_genre_counts()

c1, c2, c3 = st.columns(3)
with c1:
    kpi_card("Total Movies", len(df))
with c2:
    kpi_card("Genres", df["genre"].nunique())
with c3:
    kpi_card("Watchlist Items", len(st.session_state.watchlist))

section_header("Genre Distribution")
st.bar_chart(genre_counts)

section_header("Quick Insights")
top_genre = genre_counts.index[0] if not genre_counts.empty else "N/A"
st.markdown(f"""
<div class="glass-card">
    <p><b>Most available genre:</b> {top_genre}</p>
    <p><b>Catalog size:</b> {len(df)} titles currently loaded.</p>
    <p><b>User activity:</b> {len(st.session_state.watchlist)} movies saved to watchlist in this session.</p>
</div>
""", unsafe_allow_html=True)
