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

left, right = st.columns([1.55, 0.9])

with left:
    st.video(movie["trailer"], autoplay=True, muted=True)

with right:
    st.markdown('<div class="detail-card">', unsafe_allow_html=True)
    st.image(movie["image"], use_container_width=True)
    st.markdown(f"## {movie['title']}")
    st.markdown(f"""
    <div class="metric-chip-grid">
        <div class="metric-chip">
            <div class="label">Rating</div>
            <div class="value">⭐ {movie['rating']}</div>
        </div>
        <div class="metric-chip">
            <div class="label">Genre</div>
            <div class="value">{movie['genre']}</div>
        </div>
        <div class="metric-chip">
            <div class="label">Year</div>
            <div class="value">{movie['year']}</div>
        </div>
        <div class="metric-chip">
            <div class="label">Duration</div>
            <div class="value">{movie['duration']}</div>
        </div>
        <div class="metric-chip">
            <div class="label">Language</div>
            <div class="value">{movie['language']}</div>
        </div>
        <div class="metric-chip">
            <div class="label">Experience</div>
            <div class="value">Cinematic</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="overview-box">
        <div style="font-size:0.92rem;color:#98a8c7;margin-bottom:0.35rem;">Overview</div>
        <div>{movie['overview']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:0.9rem'></div>", unsafe_allow_html=True)

    if st.button("❤️ Add to Watchlist", key="player_watch"):
        if add_to_watchlist(movie["title"]):
            st.success(f"{movie['title']} added to watchlist")
        else:
            st.info(f"{movie['title']} already in watchlist")

    if st.button("⬅ Back to Home", key="player_back"):
        st.switch_page("pages/1_Home.py")

    st.markdown('</div>', unsafe_allow_html=True)

section_header("More Like This", "Recommendation rail from the same content profile")
recs = get_recommendations(movie["title"])

if recs.empty:
    st.info("No recommendations found.")
else:
    rec_cols = st.columns(3)
    for i, (_, row) in enumerate(recs.iterrows()):
        with rec_cols[i % 3]:
            st.markdown('<div class="poster-card">', unsafe_allow_html=True)
            st.image(row["image"], use_container_width=True)
            st.markdown(f"""
            <div class="poster-meta">
                <div class="poster-title">{row['title']}</div>
                <div class="poster-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            if st.button(f"Open {row['title']}", key=f"open_rec_{i}"):
                set_selected_movie(row.to_dict())
                st.rerun()
