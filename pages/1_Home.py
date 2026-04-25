import streamlit as st
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, hero_section, section_header, movie_card
from src.utils import initialize_session

st.set_page_config(page_title="Home | OTT Stream Pro Max", page_icon="🏠", layout="wide")

initialize_session()
inject_css()
render_sidebar()

df = load_data()

hero_section()
section_header("🔥 Trending Now")

cols = st.columns(4)
for i in range(min(8, len(df))):
    row = df.iloc[i]
    with cols[i % 4]:
        st.image(row["image"], use_container_width=True)
        movie_card(row["title"], row["genre"], row["overview"])

section_header("⭐ Spotlight Pick")
spot = df.iloc[0]

c1, c2 = st.columns([1, 1.35])
with c1:
    st.image(spot["image"], use_container_width=True)
with c2:
    st.markdown(f"""
    <div class="glass-card">
        <h2 style="margin-top:0;">{spot["title"]}</h2>
        <p class="small-note"><b>Genre:</b> {spot["genre"]}</p>
        <p>{spot["overview"]}</p>
        <p class="small-note">
            Handpicked as a featured title for the home screen showcase.
        </p>
    </div>
    """, unsafe_allow_html=True)
