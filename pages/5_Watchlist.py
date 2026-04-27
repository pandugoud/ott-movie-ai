import streamlit as st
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, topbar, section_header, poster_image, stat_card
from src.utils import initialize_session, remove_from_watchlist, set_selected_movie

st.set_page_config(page_title="Watchlist | OTT Stream Pro Max", page_icon="❤️", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()
watchlist_titles = st.session_state.watchlist

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">WATCHLIST</span>
        <span class="hero-pill">SAVE LATER</span>
        <span class="hero-pill">PERSONAL PICKS</span>
    </div>
    <div class="hero-title">
        Your saved <span class="accent">movie picks</span>
    </div>
    <div class="hero-desc">
        Keep track of titles you want to watch later and open them instantly from one place.
    </div>
</div>
""", unsafe_allow_html=True)

s1, s2 = st.columns(2, gap="large")
with s1:
    stat_card("Saved Movies", len(watchlist_titles))
with s2:
    stat_card("Total Library", len(df))

section_header("My Watchlist", "Saved content")

if not watchlist_titles:
    st.info("Watchlist empty undi. Home / Explore / AI Recommender nundi movies add cheyyandi.")
else:
    watch_df = df[df["title"].isin(watchlist_titles)].copy()

    cols = st.columns(3, gap="large")
    for i, (_, row) in enumerate(watch_df.iterrows()):
        with cols[i % 3]:
            st.markdown('<div class="grid-card">', unsafe_allow_html=True)
            poster_image(row["image"])
            st.markdown(f"""
                <div class="movie-title">{row['title']}</div>
                <div class="movie-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
                <div style="color:#91a4b7;font-size:0.88rem;line-height:1.72;">{row['overview']}</div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            a1, a2 = st.columns(2, gap="small")
            with a1:
                if st.button("🗑 Remove", key=f"remove_{i}", width="stretch"):
                    remove_from_watchlist(row["title"])
                    st.rerun()
            with a2:
                if st.button("📺 Open", key=f"watch_open_{i}", width="stretch"):
                    set_selected_movie(row.to_dict())
                    st.switch_page("pages/7_Trailer_Player.py")
