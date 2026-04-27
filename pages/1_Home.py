import streamlit as st
from src.recommender import load_data
from src.ui import inject_css, render_sidebar, topbar, section_header, stat_card
from src.utils import (
    initialize_session,
    add_to_watchlist,
    set_selected_movie,
    next_feature,
    prev_feature
)

st.set_page_config(
    page_title="Home | OTT Stream Pro Max",
    page_icon="🏠",
    layout="wide"
)

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
            <span class="hero-pill">PREMIUM UI</span>
            <span class="hero-pill">MOOD AI</span>
        </div>
        <div class="hero-title">
            Discover your next <span class="accent">favorite movie</span> in seconds
        </div>
        <div class="hero-desc">
            Browse a premium OTT-inspired movie experience with quick discovery, mood-based recommendations,
            smart similarity suggestions, trailer previews, and watchlist support.
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

    a1, a2, a3, a4 = st.columns(4, gap="small")
    with a1:
        if st.button("📺 Open Now", key="hero_open", width="stretch"):
            set_selected_movie(featured.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")
    with a2:
        if st.button("❤️ Save", key="hero_save", width="stretch"):
            if add_to_watchlist(featured["title"]):
                st.success(f"{featured['title']} added")
            else:
                st.info("Already added")
    with a3:
        if st.button("⬅ Prev", key="hero_prev", width="stretch"):
            prev_feature(len(df))
            st.rerun()
    with a4:
        if st.button("Next ➜", key="hero_next", width="stretch"):
            next_feature(len(df))
            st.rerun()

with hero_right:
    st.markdown('<div class="hero-poster-box">', unsafe_allow_html=True)
    st.markdown('<div class="poster-frame">', unsafe_allow_html=True)
    st.image(featured["image"], width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="movie-title" style="font-size:1.18rem; margin-top:0.9rem;">{featured['title']}</div>
        <div class="movie-sub">{featured['genre']} • {featured['year']} • <span class="mini-stat">⭐ {featured['rating']}</span></div>
        <div style="color:#94a3b8; line-height:1.8; font-size:0.93rem;">
            {featured['overview']}
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

section_header("Platform Snapshot", "Quick highlights from your app")
s1, s2, s3, s4 = st.columns(4, gap="large")
with s1:
    stat_card("Total Movies", len(df))
with s2:
    stat_card("Genres Covered", df["genre"].nunique())
with s3:
    stat_card("Languages", df["language"].nunique())
with s4:
    stat_card("Watchlist Items", len(st.session_state.watchlist))

st.markdown('<div class="glass-divider"></div>', unsafe_allow_html=True)

section_header("Trending Now", "Quick access to popular picks")

trend_cols = st.columns(5, gap="medium")
for i, (_, row) in enumerate(df.head(5).iterrows()):
    with trend_cols[i]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        st.markdown('<div class="poster-frame">', unsafe_allow_html=True)
        st.image(row["image"], width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['year']}</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Open", key=f"trend_open_{i}", width="stretch"):
            set_selected_movie(row.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")

st.markdown('<div class="glass-divider"></div>', unsafe_allow_html=True)

section_header("Top Picks For You", "Beautiful cards with fast actions")

cards = st.columns(4, gap="large")
for i in range(min(8, len(df))):
    row = df.iloc[i]
    with cards[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        st.markdown('<div class="poster-frame">', unsafe_allow_html=True)
        st.image(row["image"], width="stretch")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['language']} • <span class="mini-stat">⭐ {row['rating']}</span></div>
            <div style="color:#94a3b8; font-size:0.88rem; line-height:1.75;">
                {row['overview']}
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="small")
        with c1:
            if st.button("❤️ Watchlist", key=f"home_watch_{i}", width="stretch"):
                if add_to_watchlist(row["title"]):
                    st.success("Added")
                else:
                    st.info("Already added")
        with c2:
            if st.button("📺 Open", key=f"home_detail_{i}", width="stretch"):
                set_selected_movie(row.to_dict())
                st.switch_page("pages/7_Trailer_Player.py")

st.markdown('<div class="glass-divider"></div>', unsafe_allow_html=True)

section_header("Explore More", "Open other sections of the app")
n1, n2, n3, n4 = st.columns(4, gap="small")
with n1:
    if st.button("🔎 Explore", key="home_nav_explore", width="stretch"):
        st.switch_page("pages/2_Explore.py")
with n2:
    if st.button("🤖 AI Recommender", key="home_nav_ai", width="stretch"):
        st.switch_page("pages/3_AI_Recommender.py")
with n3:
    if st.button("❤️ Watchlist", key="home_nav_watchlist", width="stretch"):
        st.switch_page("pages/5_Watchlist.py")
with n4:
    if st.button("ℹ️ About Us", key="home_nav_about", width="stretch"):
        st.switch_page("pages/4_About_Us.py")
