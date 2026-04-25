import streamlit as st
from streamlit_clickable_images import clickable_images
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, hero_section, section_header, movie_card
from src.utils import initialize_session, play_movie, stop_movie, is_playing, add_to_watchlist

st.set_page_config(page_title="Home | OTT Stream Pro Max", page_icon="🏠", layout="wide")

initialize_session()
inject_css()
render_sidebar()

df = load_data()
hero_section()

section_header("🔥 Click Poster to Play Trailer")

images = df["image"].tolist()
titles = df["title"].tolist()

clicked = clickable_images(
    images,
    titles=titles,
    div_style={
        "display": "flex",
        "justify-content": "flex-start",
        "flex-wrap": "wrap",
        "gap": "14px"
    },
    img_style={
        "height": "260px",
        "border-radius": "18px",
        "cursor": "pointer",
        "box-shadow": "0 12px 25px rgba(0,0,0,0.30)",
        "border": "1px solid rgba(255,255,255,0.08)"
    },
    key="home_clickable_posters"
)

if clicked > -1:
    selected_title = df.iloc[clicked]["title"]
    play_movie(selected_title)

if st.session_state.playing_movie:
    current = df[df["title"] == st.session_state.playing_movie].iloc[0]
    section_header(f"▶ Now Playing: {current['title']}")
    st.markdown('<div class="video-frame">', unsafe_allow_html=True)
    st.video(current["trailer"], autoplay=True, muted=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("❌ Close Trailer", key="close_home_trailer"):
            stop_movie()
            st.rerun()
    with col2:
        if st.button("❤️ Add to Watchlist", key="add_home_watchlist"):
            added = add_to_watchlist(current["title"])
            if added:
                st.success(f"{current['title']} added to watchlist")
            else:
                st.info(f"{current['title']} already in watchlist")

section_header("⭐ Trending Picks")
cols = st.columns(4)

for i in range(min(8, len(df))):
    row = df.iloc[i]
    with cols[i % 4]:
        if is_playing(row["title"]):
            st.video(row["trailer"], autoplay=True, muted=True)
            if st.button(f"Close {row['title']}", key=f"close_trending_{i}"):
                stop_movie()
                st.rerun()
        else:
            st.image(row["image"], use_container_width=True)
            movie_card(row["title"], row["genre"], row["overview"])

            if st.button(f"▶ Play {row['title']}", key=f"play_trending_{i}"):
                play_movie(row["title"])
                st.rerun()

            if st.button(f"❤️ Save {row['title']}", key=f"save_trending_{i}"):
                added = add_to_watchlist(row["title"])
                if added:
                    st.success("Added")
                else:
                    st.info("Already in watchlist")
