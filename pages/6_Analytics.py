import streamlit as st
from src.recommender import load_data, get_genre_counts, get_language_counts, get_top_rated
from src.ui import inject_css, render_sidebar, topbar, section_header, stat_card, poster_image
from src.utils import initialize_session, set_selected_movie

st.set_page_config(page_title="Analytics | OTT Stream Pro Max", page_icon="📊", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()
genre_counts = get_genre_counts()
language_counts = get_language_counts()
top_rated = get_top_rated(4)

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">ANALYTICS</span>
        <span class="hero-pill">INSIGHTS</span>
        <span class="hero-pill">LIBRARY OVERVIEW</span>
    </div>
    <div class="hero-title">
        Quick insights from your <span class="accent">movie library</span>
    </div>
    <div class="hero-desc">
        View content counts, top genres, language mix, and top-rated titles from the current dataset.
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="large")
with c1:
    stat_card("Total Movies", len(df))
with c2:
    stat_card("Genres", genre_counts.shape[0])
with c3:
    stat_card("Languages", language_counts.shape[0])
with c4:
    stat_card("Top Genre", genre_counts.index[0] if len(genre_counts) else "N/A")

section_header("Genre Distribution", "Movies by genre")
st.bar_chart(genre_counts)

section_header("Language Distribution", "Movies by language")
st.bar_chart(language_counts)

section_header("Top Rated Titles", "Highest rated content in the dataset")
cols = st.columns(4, gap="large")
for i, (_, row) in enumerate(top_rated.iterrows()):
    with cols[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        poster_image(row["image"])
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['language']} • <span class="mini-stat">⭐ {row['rating']}</span></div>
            <div style="color:#91a4b7;font-size:0.88rem;line-height:1.72;">{row['overview']}</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("📺 Open", key=f"analytics_open_{i}", width="stretch"):
            set_selected_movie(row.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")
