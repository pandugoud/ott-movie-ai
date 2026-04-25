import streamlit as st
from src.recommender import search_movies
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, add_to_watchlist, set_selected_movie

st.set_page_config(page_title="Explore | OTT Stream Pro Max", page_icon="🔎", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

section_header("Explore Movies", "Search by title, genre, language, year or overview")

query = st.text_input("Search movies", placeholder="Search Inception, Action, Telugu, 2022...")
results = search_movies(query)

if query.strip():
    st.write(f"Results found: {len(results)}")
else:
    st.write(f"Showing all movies: {len(results)}")

cols = st.columns(4, gap="large")
for i, (_, row) in enumerate(results.iterrows()):
    with cols[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        st.image(row["image"], width="stretch")
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['language']} • ⭐ {row['rating']}</div>
            <div style="color:#a7bac7;font-size:0.88rem;line-height:1.6;">{row['overview']}</div>
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
