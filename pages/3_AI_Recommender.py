import streamlit as st
from src.recommender import load_data, get_recommendations
from src.ui import inject_css, render_sidebar, section_header, movie_card
from src.utils import initialize_session, add_to_watchlist, get_trailer

st.set_page_config(page_title="AI Recommender | OTT Stream Pro Max", page_icon="🤖", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("🤖 AI Movie Recommender")

df = load_data()
movie_list = sorted(df["title"].dropna().unique().tolist())
selected_movie = st.selectbox("Choose a movie you like", movie_list)

if st.button("Get Smart Recommendations"):
    recs = get_recommendations(selected_movie)

    if recs.empty:
        st.warning("No recommendations found.")
    else:
        section_header(f"Because you watched {selected_movie}")
        cols = st.columns(3)

        for i, (_, row) in enumerate(recs.iterrows()):
            with cols[i % 3]:
                st.image(row["image"], use_container_width=True)
                movie_card(row["title"], row["genre"], row["overview"])

                trailer_url = get_trailer(row["title"])
                if trailer_url:
                    st.markdown(
                        f"[▶ Watch Trailer]({trailer_url})",
                        unsafe_allow_html=False
                    )

                if st.button(f"❤️ Save {row['title']}", key=f"rec_add_{i}"):
                    added = add_to_watchlist(row["title"])
                    if added:
                        st.success(f"{row['title']} saved")
                    else:
                        st.info(f"{row['title']} already in watchlist")
