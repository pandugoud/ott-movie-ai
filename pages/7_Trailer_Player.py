import streamlit as st
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, add_to_watchlist

st.set_page_config(page_title="Trailer Player | OTT Stream Pro Max", page_icon="🎞️", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

movie = st.session_state.get("selected_movie", None)

if not movie:
    st.warning("No movie selected. Home / Explore / AI page nundi oka movie open cheyyandi.")
    if st.button("⬅ Go Home", key="go_home_empty", width="stretch"):
        st.switch_page("pages/1_Home.py")
    st.stop()

section_header(movie["title"], "Trailer and movie details")

left, right = st.columns([1.2, 0.8], gap="large")

with left:
    st.markdown('<div class="hero-v2">', unsafe_allow_html=True)
    st.video(movie["trailer"])
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="hero-v2">', unsafe_allow_html=True)
    st.image(movie["image"], width="stretch")
    st.markdown(f"""
        <div class="movie-title" style="font-size:1.2rem;">{movie['title']}</div>
        <div class="movie-sub">{movie['genre']} • {movie['year']} • {movie['duration']} • {movie['language']} • ⭐ {movie['rating']}</div>
        <div style="color:#a7bac7;line-height:1.8;">{movie['overview']}</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

a1, a2, a3 = st.columns(3, gap="small")
with a1:
    if st.button("❤️ Add Watchlist", key="detail_watch", width="stretch"):
        if add_to_watchlist(movie["title"]):
            st.success("Added to watchlist")
        else:
            st.info("Already added")
with a2:
    if st.button("🏠 Home", key="detail_home", width="stretch"):
        st.switch_page("pages/1_Home.py")
with a3:
    if st.button("🔎 Explore", key="detail_explore", width="stretch"):
        st.switch_page("pages/2_Explore.py")
