import streamlit as st
from src.recommender import search_movies, load_data
from src.ui import inject_css, render_sidebar, section_header, movie_card
from src.utils import initialize_session, play_movie, stop_movie, is_playing, add_to_watchlist

st.set_page_config(page_title="Explore | OTT Stream Pro Max", page_icon="🔎", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("🔎 Explore Movies")

df = load_data()
genres = ["All"] + sorted(df["genre"].unique().tolist())
query = st.text_input("Search movie, genre, or overview")
selected_genre = st.selectbox("Genre Filter", genres)

filtered = search_movies(query)
if selected_genre != "All":
    filtered = filtered[filtered["genre"] == selected_genre]

section_header(f"Results ({len(filtered)})")

if filtered.empty:
    st.warning("No movies found.")
else:
    cols = st.columns(3)
    for i, (_, row) in enumerate(filtered.iterrows()):
        with cols[i % 3]:
            if is_playing(row["title"]):
                st.video(row["trailer"], autoplay=True, muted=True)
                if st.button(f"❌ Close {row['title']}", key=f"close_explore_{i}"):
                    stop_movie()
                    st.rerun()
            else:
                st.image(row["image"], use_container_width=True)
                movie_card(row["title"], row["genre"], row["overview"])

                if st.button(f"▶ Play Trailer {row['title']}", key=f"play_explore_{i}"):
                    play_movie(row["title"])
                    st.rerun()

                if st.button(f"❤️ Watchlist {row['title']}", key=f"watch_explore_{i}"):
                    added = add_to_watchlist(row["title"])
                    if added:
                        st.success(f"{row['title']} added")
                    else:
                        st.info("Already exists")
