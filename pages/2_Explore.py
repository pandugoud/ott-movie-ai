import streamlit as st
from src.recommender import search_movies, load_data
from src.ui import inject_css, render_sidebar, topbar, section_header, stat_card, poster_image
from src.utils import initialize_session, add_to_watchlist, set_selected_movie

st.set_page_config(page_title="Explore | OTT Stream Pro Max", page_icon="🔎", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">EXPLORE</span>
        <span class="hero-pill">SEARCH</span>
        <span class="hero-pill">DISCOVERY</span>
    </div>
    <div class="hero-title">
        Search movies with a <span class="accent">cleaner premium grid</span>
    </div>
    <div class="hero-desc">
        Search by title, genre, language, year, or overview and browse results in a richer card layout.
    </div>
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3, gap="large")
with s1:
    stat_card("Total Library", len(df))
with s2:
    stat_card("Genres", df["genre"].nunique())
with s3:
    stat_card("Languages", df["language"].nunique())

section_header("Find Movies", "Search and browse your full library")
query = st.text_input("Search movies", placeholder="Search Inception, Telugu, Action, 2022...")
results = search_movies(query)

if query.strip():
    st.caption(f"Results found: {len(results)}")
else:
    st.caption(f"Showing all movies: {len(results)}")

cols = st.columns(4, gap="large")
for i, (_, row) in enumerate(results.iterrows()):
    with cols[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        poster_image(row["image"])
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['language']} • ⭐ {row['rating']}</div>
            <div style="color:#91a4b7;font-size:0.88rem;line-height:1.72;">{row['overview']}</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="small")
        with c1:
            if st.button("❤️ Watchlist", key=f"explore_watch_{i}", width="stretch"):
                if add_to_watchlist(row["title"]):
                    st.success("Added")
                else:
                    st.info("Already added")
        with c2:
            if st.button("📺 Open", key=f"explore_open_{i}", width="stretch"):
                set_selected_movie(row.to_dict())
                st.switch_page("pages/7_Trailer_Player.py")
