import streamlit as st
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, section_header, movie_card
from src.utils import initialize_session, remove_from_watchlist, play_movie, stop_movie, is_playing

st.set_page_config(page_title="Watchlist | OTT Stream Pro Max", page_icon="❤️", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("❤️ My Watchlist")
section_header("Saved Movies")

df = load_data()

if not st.session_state.watchlist:
    st.info("Your watchlist is empty.")
else:
    saved_df = df[df["title"].isin(st.session_state.watchlist)]

    cols = st.columns(3)
    for i, (_, row) in enumerate(saved_df.iterrows()):
        with cols[i % 3]:
            if is_playing(row["title"]):
                st.video(row["trailer"], autoplay=True, muted=True)
                if st.button(f"❌ Close {row['title']}", key=f"close_watch_{i}"):
                    stop_movie()
                    st.rerun()
            else:
                st.image(row["image"], use_container_width=True)
                movie_card(row["title"], row["genre"], row["overview"])

                if st.button(f"▶ Play {row['title']}", key=f"play_watch_{i}"):
                    play_movie(row["title"])
                    st.rerun()

                if st.button(f"Remove {row['title']}", key=f"remove_watch_{i}"):
                    remove_from_watchlist(row["title"])
                    st.rerun()
