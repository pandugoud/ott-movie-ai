import streamlit as st
from src.recommender import load_data, search_movies
from src.ui import inject_css, render_sidebar, section_header, movie_card
from src.utils import initialize_session, add_to_watchlist

st.set_page_config(page_title="Explore | OTT Stream Pro Max", page_icon="🔎", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("🔎 Explore Movies")

df = load_data()
genres = ["All"] + sorted(df["genre"].dropna().unique().tolist())

query = st.text_input("Search by movie, genre, or overview")
selected_genre = st.selectbox("Filter by genre", genres)

filtered = search_movies(query)

if selected_genre != "All":
    filtered = filtered[filtered["genre"] == selected_genre]

section_header(f"Results ({len(filtered)})")

if filtered.empty:
    st.warning("No movies found. Try another search keyword.")
else:
    cols = st.columns(3)
    for i, (_, row) in enumerate(filtered.iterrows()):
        with cols[i % 3]:
            st.image(row["image"], use_container_width=True)
            movie_card(row["title"], row["genre"], row["overview"])
            if st.button(f"➕ Add {row['title']}", key=f"explore_add_{i}"):
                added = add_to_watchlist(row["title"])
                if added:
                    st.success(f"{row['title']} added to watchlist")
                else:
                    st.info(f"{row['title']} already in watchlist")
