import streamlit as st
from streamlit_clickable_images import clickable_images
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, hero_section, section_header, movie_card
from src.utils import initialize_session, add_to_watchlist

st.set_page_config(page_title="Home | OTT Stream Pro Max", page_icon="🏠", layout="wide")

initialize_session()
inject_css()
render_sidebar()

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

df = load_data()

@st.dialog("🎬 Watch Trailer")
def show_trailer_popup(movie):
    st.subheader(movie["title"])
    st.caption(f"Genre: {movie['genre']}")
    st.video(movie["trailer"], autoplay=True, muted=True)
    st.write(movie["overview"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("❤️ Add to Watchlist", key=f"popup_watch_{movie['title']}"):
            if add_to_watchlist(movie["title"]):
                st.success(f"{movie['title']} added to watchlist")
            else:
                st.info(f"{movie['title']} already in watchlist")

    with col2:
        if st.button("📺 Open Full Player Page", key=f"popup_page_{movie['title']}"):
            st.session_state.selected_movie = movie.to_dict()
            st.switch_page("pages/7_Trailer_Player.py")

st.title("🏠 Home")
hero_section()
section_header("🔥 Click Poster")

clicked = clickable_images(
    df["image"].tolist(),
    titles=df["title"].tolist(),
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
    key="home_posters_click"
)

if clicked > -1:
    movie = df.iloc[clicked]
    show_trailer_popup(movie)

section_header("⭐ Trending Picks")

cols = st.columns(4)

for i in range(min(8, len(df))):
    row = df.iloc[i]

    with cols[i % 4]:
        st.image(row["image"], use_container_width=True)
        movie_card(row["title"], row["genre"], row["overview"])

        if st.button(f"▶ Popup Play - {row['title']}", key=f"popup_btn_{i}"):
            show_trailer_popup(row)

        if st.button(f"📺 Next Page - {row['title']}", key=f"page_btn_{i}"):
            st.session_state.selected_movie = row.to_dict()
            st.switch_page("pages/7_Trailer_Player.py")

        if st.button(f"❤️ Save - {row['title']}", key=f"save_btn_{i}"):
            if add_to_watchlist(row["title"]):
                st.success("Added to watchlist")
            else:
                st.info("Already in watchlist")
