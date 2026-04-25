import streamlit as st
from src.ui import inject_css, render_sidebar, section_header
from src.utils import initialize_session, add_to_watchlist

st.set_page_config(page_title="Trailer Player | OTT Stream Pro Max", page_icon="🎬", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("🎬 Trailer Player")

if "selected_movie" not in st.session_state or st.session_state.selected_movie is None:
    st.warning("No movie selected. Please go back to Home and choose a movie.")
    if st.button("⬅ Back to Home"):
        st.switch_page("app.py")
    st.stop()

movie = st.session_state.selected_movie

section_header("Now Playing")

col1, col2 = st.columns([1.4, 1])

with col1:
    st.video(movie["trailer"], autoplay=True, muted=True)

with col2:
    st.image(movie["image"], use_container_width=True)
    st.subheader(movie["title"])
    st.write(f"**Genre:** {movie['genre']}")
    st.write(movie["overview"])

    if st.button("❤️ Add to Watchlist"):
        if add_to_watchlist(movie["title"]):
            st.success(f"{movie['title']} added to watchlist")
        else:
            st.info(f"{movie['title']} already in watchlist")

    if st.button("⬅ Back to Home"):
        st.switch_page("app.py")
