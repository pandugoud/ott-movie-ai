import streamlit as st
from src.recommender import get_recommendations
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, add_to_watchlist, set_selected_movie

st.set_page_config(page_title="Trailer Player | OTT Stream Pro Max", page_icon="🎬", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

if not st.session_state.selected_movie:
    st.warning("No movie selected. Go to Home page and choose a movie.")
    if st.button("⬅ Back to Home"):
        st.switch_page("pages/1_Home.py")
    st.stop()

movie = st.session_state.selected_movie

section_header("Now Streaming", "Full OTT-style detail layout with trailer, metadata, and recommendations")

left, right = st.columns([1.55, 0.9], gap="large")

with left:
    st.video(movie["trailer"], autoplay=True, muted=True)

with right:
    st.image(movie["image"], width="stretch")
    st.markdown(f"## {movie['title']}")
    st.markdown(f"**Genre:** {movie['genre']}")
    st.markdown(f"**Year:** {movie['year']}")
    st.markdown(f"**Duration:** {movie['duration']}")
    st.markdown(f"**Language:** {movie['language']}")
    st.markdown(f"**Rating:** ⭐ {movie['rating']}")
    st.write(movie["overview"])

    if st.button("❤️ Add to Watchlist", key="player_watch"):
        if add_to_watchlist(movie["title"]):
            st.success(f"{movie['title']} added to watchlist")
        else:
            st.info("Already in watchlist")

    if st.button("⬅ Back to Home", key="player_back"):
        st.switch_page("pages/1_Home.py")

section_header("More Like This", "Recommendation rail")
recs = get_recommendations(movie["title"])

if recs.empty:
    st.info("No recommendations found.")
else:
    rec_cols = st.columns(3, gap="large")
    for i, (_, row) in enumerate(recs.iterrows()):
        with rec_cols[i % 3]:
            st.markdown('<div class="grid-card">', unsafe_allow_html=True)
            st.image(row["image"], width="stretch")
            st.markdown(f"""
                <div class="movie-title">{row['title']}</div>
                <div class="movie-sub">{row['genre']} • {row['year']} • <span class="mini-stat">⭐ {row['rating']}</span></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            if st.button(f"Open {row['title']}", key=f"rec_{i}"):
                set_selected_movie(row.to_dict())
                st.rerun()
