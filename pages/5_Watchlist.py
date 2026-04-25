import streamlit as st
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, remove_from_watchlist, set_selected_movie

st.set_page_config(page_title="Watchlist | OTT Stream Pro Max", page_icon="❤️", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()

section_header("My Watchlist", "Mee saved movies ikkada untayi")

watchlist_titles = st.session_state.watchlist

if not watchlist_titles:
    st.info("Watchlist empty undi. Home / Explore / AI Recommender nundi movies add cheyyandi.")
else:
    watch_df = df[df["title"].isin(watchlist_titles)].copy()

    cols = st.columns(3, gap="large")
    for i, (_, row) in enumerate(watch_df.iterrows()):
        with cols[i % 3]:
            st.markdown('<div class="grid-card">', unsafe_allow_html=True)
            st.image(row["image"], width="stretch")
            st.markdown(f"""
                <div class="movie-title">{row['title']}</div>
                <div class="movie-sub">{row['genre']} • {row['language']} • ⭐ {row['rating']}</div>
                <div style="color:#9aa8c3;font-size:0.88rem;line-height:1.6;">{row['overview']}</div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            with c1:
                if st.button("🗑 Remove", key=f"remove_watch_{i}"):
                    if remove_from_watchlist(row["title"]):
                        st.success("Removed")
                        st.rerun()
            with c2:
                if st.button("📺 Open", key=f"watch_open_{i}"):
                    set_selected_movie(row.to_dict())
                    st.switch_page("pages/7_Trailer_Player.py")
