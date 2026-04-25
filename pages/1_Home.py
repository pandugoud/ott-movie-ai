import streamlit as st
from st_clickable_images import clickable_images
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

@st.dialog("🎬 Trailer Preview", width="large")
def show_trailer_popup(movie):
    st.markdown("<span class='dialog-anchor'></span>", unsafe_allow_html=True)

    left, right = st.columns([1.45, 0.95], gap="large")
    with left:
        st.video(movie["trailer"], autoplay=True, muted=True)

    with right:
        st.image(movie["image"], use_container_width=True)
        st.markdown(f"### {movie['title']}")
        st.markdown(f"**{movie['year']} • {movie['duration']} • {movie['language']} • ⭐ {movie['rating']}**")
        st.write(movie["overview"])

        st.markdown(
            f"""
            <span class="watch-chip">{movie['genre']}</span>
            <span class="watch-chip">Featured Pick</span>
            <span class="watch-chip">Popup Trailer</span>
            """,
            unsafe_allow_html=True
        )

        if st.button("❤️ Add to Watchlist", key=f"dlg_watch_{movie['title']}"):
            if add_to_watchlist(movie["title"]):
                st.success(f"{movie['title']} added to watchlist")
            else:
                st.info("Already in watchlist")

        if st.button("📺 Open Full Detail Page", key=f"dlg_open_{movie['title']}"):
            set_selected_movie(movie.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")


hero_left, hero_right = st.columns([1.15, 0.85], gap="large")

with hero_left:
    st.markdown("""
    <div class="hero-v2">
        <div class="hero-left">
            <div class="hero-pills">
                <span class="hero-pill">FEATURED TODAY</span>
                <span class="hero-pill">POPUP TRAILER</span>
                <span class="hero-pill">FULL DETAIL PAGE</span>
                <span class="hero-pill">AI RECOMMENDATIONS</span>
            </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="hero-title">
            Watch <span class="accent">{featured['title']}</span> in a premium OTT-style experience
        </div>
        <div class="hero-desc">
            Explore trailers in a large cinematic popup, save movies to your watchlist,
            and jump into a full OTT detail page with recommendations.
        </div>
        <div class="hero-meta">
            <span class="meta-chip">⭐ {featured['rating']}</span>
            <span class="meta-chip">{featured['genre']}</span>
            <span class="meta-chip">{featured['year']}</span>
            <span class="meta-chip">{featured['duration']}</span>
            <span class="meta-chip">{featured['language']}</span>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns([1.1, 1.15, 0.8, 0.8])
    with c1:
        if st.button("▶ Play Trailer", key="hero_popup"):
            show_trailer_popup(featured)
    with c2:
        if st.button("📺 Full Detail Page", key="hero_page"):
            set_selected_movie(featured.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")
    with c3:
        if st.button("⬅ Prev", key="hero_prev"):
            prev_feature(len(df))
            st.rerun()
    with c4:
        if st.button("Next ➜", key="hero_next"):
            next_feature(len(df))
            st.rerun()

    st.markdown("</div></div>", unsafe_allow_html=True)

with hero_right:
    st.markdown('<div class="hero-v2"><div class="hero-poster-box">', unsafe_allow_html=True)
    st.image(featured["image"], use_container_width=True)
    st.markdown(f"""
        <div class="movie-title">{featured['title']}</div>
        <div class="movie-sub">{featured['genre']} • {featured['year']} • <span class="mini-stat">⭐ {featured['rating']}</span></div>
        <div class="compact-note">
            {featured['overview']}
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

section_header("Trending Now", "Click any poster for instant popup trailer preview")
st.markdown('<div class="rail-card">', unsafe_allow_html=True)

clicked = clickable_images(
    df["image"].tolist(),
    titles=[f"{row['title']} ({row['year']})" for _, row in df.iterrows()],
    div_style={
        "display": "flex",
        "justify-content": "flex-start",
        "flex-wrap": "wrap",
        "gap": "12px"
    },
    img_style={
        "height": "250px",
        "border-radius": "16px",
        "cursor": "pointer",
        "box-shadow": "0 10px 20px rgba(0,0,0,0.28)",
        "border": "1px solid rgba(255,255,255,0.06)"
    },
    key="trending_click_row_v2"
)

if clicked > -1:
    show_trailer_popup(df.iloc[clicked])

st.markdown("</div>", unsafe_allow_html=True)

section_header("Top Picks", "Cleaner cards with compact actions")
cards = st.columns(4, gap="large")

for i in range(min(8, len(df))):
    row = df.iloc[i]

    with cards[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        st.image(row["image"], use_container_width=True)
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['year']} • <span class="mini-stat">⭐ {row['rating']}</span></div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        a1, a2 = st.columns(2, gap="small")
        with a1:
            if st.button("▶ Play", key=f"play_{i}"):
                show_trailer_popup(row)
        with a2:
            if st.button("📺 Details", key=f"details_{i}"):
                set_selected_movie(row.to_dict())
                st.switch_page("pages/7_Trailer_Player.py")
