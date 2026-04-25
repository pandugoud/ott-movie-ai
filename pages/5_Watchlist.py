import streamlit as st
from src.ui import inject_css, render_sidebar, section_header
from src.utils import initialize_session, remove_from_watchlist

st.set_page_config(page_title="Watchlist | OTT Stream Pro Max", page_icon="❤️", layout="wide")

initialize_session()
inject_css()
render_sidebar()

st.title("❤️ My Watchlist")
section_header("Saved Movies")

if not st.session_state.watchlist:
    st.info("Your watchlist is empty. Add movies from Explore or AI Recommender.")
else:
    for i, movie in enumerate(st.session_state.watchlist):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            <div class="glass-card" style="margin-bottom:0.8rem;">
                <h4 style="margin:0;">🎬 {movie}</h4>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("Remove", key=f"remove_{i}"):
                remove_from_watchlist(movie)
                st.rerun()
