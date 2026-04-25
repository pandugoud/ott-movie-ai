import streamlit as st
from src.recommender import load_data, get_recommendations
from src.ui import inject_css, render_sidebar, section_header, movie_card
from src.utils import initialize_session, play_movie, stop_movie, is_playing, add_to_watchlist

st.set_page_config(page_title="AI Recommender | OTT Stream Pro Max", page_icon="🤖", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("🤖 AI Movie Recommender")

df = load_data()
movie_list = sorted(df["title"].dropna().unique().tolist())
selected_movie = st.selectbox("Choose your favorite movie", movie_list)

if st.button("Get Recommendations"):
    st.session_state["last_selected_movie"] = selected_movie

if "last_selected_movie" in st.session_state:
    recs = get_recommendations(st.session_state["last_selected_movie"])
    section_header(f"Recommended because you like {st.session_state['last_selected_movie']}")

    if recs.empty:
        st.warning("No recommendations found.")
    else:
        cols = st.columns(3)
        for i, (_, row) in enumerate(recs.iterrows()):
            with cols[i % 3]:
                if is_playing(row["title"]):
                    st.video(row["trailer"], autoplay=True, muted=True)
                    if st.button(f"❌ Close {row['title']}", key=f"close_rec_{i}"):
                        stop_movie()
                        st.rerun()
                else:
                    st.image(row["image"], use_container_width=True)
                    movie_card(row["title"], row["genre"], row["overview"])

                    if st.button(f"▶ Play {row['title']}", key=f"play_rec_{i}"):
                        play_movie(row["title"])
                        st.rerun()

                    if st.button(f"❤️ Save {row['title']}", key=f"save_rec_{i}"):
                        added = add_to_watchlist(row["title"])
                        if added:
                            st.success("Saved")
                        else:
                            st.info("Already saved")
