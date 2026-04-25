import streamlit as st
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, add_to_watchlist, set_selected_movie, next_feature, prev_feature

st.set_page_config(page_title="Home | OTT Stream Pro Max", page_icon="🏠", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()
featured = df.iloc[st.session_state.featured_index % len(df)]

hero_left, hero_right = st.columns([1.15, 0.85], gap="large")

with hero_left:
    st.markdown(f"""
    <div class="hero-v2">
        <div class="hero-pills">
            <span class="hero-pill">FEATURED TODAY</span>
            <span class="hero-pill">MOOD AI</span>
            <span class="hero-pill">SMART DISCOVERY</span>
        </div>
        <div class="hero-title">
            Watch <span class="accent">{featured['title']}</span> in a premium OTT-style experience
        </div>
        <div class="hero-desc">
            Explore featured movies, open full trailer pages, and discover recommendations by vibe.
        </div>
        <div class="hero-meta">
            <span class="meta-chip">⭐ {featured['rating']}</span>
            <span class="meta-chip">{featured['genre']}</span>
            <span class="meta-chip">{featured['year']}</span>
            <span class="meta-chip">{featured['duration']}</span>
            <span class="meta-chip">{featured['language']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        if st.button("📺 Open Detail", key="hero_page", width="stretch"):
            set_selected_movie(featured.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")
    with c2:
        if st.button("❤️ Add Watchlist", key="hero_watch", width="stretch"):
            if add_to_watchlist(featured["title"]):
                st.success(f"{featured['title']} added")
            else:
                st.info("Already added")
    with c3:
        if st.button("⬅ Prev", key="hero_prev", width="stretch"):
            prev_feature(len(df))
            st.rerun()
    with c4:
        if st.button("Next ➜", key="hero_next", width="stretch"):
            next_feature(len(df))
            st.rerun()

with hero_right:
    st.markdown('<div class="hero-v2"><div class="hero-poster-box">', unsafe_allow_html=True)
    st.image(featured["image"], width="stretch")
    st.markdown(f"""
        <div class="movie-title">{featured['title']}</div>
        <div class="movie-sub">{featured['genre']} • {featured['year']} • <span class="mini-stat">⭐ {featured['rating']}</span></div>
        <div style="color:#a7bac7;">{featured['overview']}</div>
    """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

section_header("Trending Now", "Quick picks")
cols = st.columns(5, gap="medium")
for i, (_, row) in enumerate(df.head(5).iterrows()):
    with cols[i]:
        st.image(row["image"], width="stretch")
        if st.button(f"Open {row['title']}", key=f"home_open_{i}", width="stretch"):
            set_selected_movie(row.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")

section_header("Top Picks", "Premium cards with quick actions")
cards = st.columns(4, gap="large")
for i in range(min(8, len(df))):
    row = df.iloc[i]
    with cards[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        st.image(row["image"], width="stretch")
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['year']} • <span class="mini-stat">⭐ {row['rating']}</span></div>
            <div style="color:#a7bac7;font-size:0.88rem;line-height:1.6;">{row['overview']}</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        a1, a2 = st.columns(2, gap="small")
        with a1:
            if st.button("❤️ Watchlist", key=f"home_watch_{i}", width="stretch"):
                if add_to_watchlist(row["title"]):
                    st.success("Added")
                else:
                    st.info("Already added")
        with a2:
            if st.button("📺 Open", key=f"home_detail_{i}", width="stretch"):
                set_selected_movie(row.to_dict())
                st.switch_page("pages/7_Trailer_Player.py")
