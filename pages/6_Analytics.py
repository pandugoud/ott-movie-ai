import streamlit as st
from src.recommender import load_data, get_genre_counts
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session

st.set_page_config(page_title="Analytics | OTT Stream Pro Max", page_icon="📊", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

section_header("Analytics", "Movie dataset overview")

df = load_data()
genre_counts = get_genre_counts()

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Total Movies", len(df))
with c2:
    st.metric("Total Genres", genre_counts.shape[0])
with c3:
    st.metric("Top Genre", genre_counts.index[0] if len(genre_counts) else "N/A")

st.subheader("Genre Counts")
st.bar_chart(genre_counts)
