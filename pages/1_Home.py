import streamlit as st
from streamlit_clickable_images import clickable_images
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
    st.markdown("<span class='cinema-dialog-anchor'></span>", unsafe_allow_html=True)

    c1, c2 = st.columns([1.55, 0.95])
    with c1:
        st.video(movie["trailer"], autoplay=True, muted=True)
    with c2:
        st.image(movie["image"], use_container_width=True)
        st.markdown(f"### {movie['title']}")
        st.markdown(
            f"**{movie['year']} • {movie['duration']} • {movie['language']} • ⭐ {movie['rating']}**"
        )
        st.write(movie["overview"])

        if st.button("❤️ Add to Watchlist", key=f"dlg_watch_{movie['title']}"):
            if add_to_watchlist(movie["title"]):
                st.success(f"{movie['title']} added")
            else:
                st.info("Already in watchlist")

        if st.button("📺 Open Full OTT Detail Page", key=f"dlg_open_{movie['title']}"):
            set_selected_movie(movie.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")

st.markdown(f"""
<div class="hero-shell">
    <div class="hero-grid">
        <div>
            <div class="hero-pill-row">
                <span class="hero-pill">FEATURED TODAY</span>
                <span class="hero-pill">CINEMATIC POPUP</span>
                <span class="hero-pill">FULL DETAIL PAGE</span>
                <span class="hero-pill">AI RECOMMENDATIONS</span>
            </div>
            <div class="hero-title">
                Watch <span class="accent">{featured['title']}</span> in a premium OTT-style experience
            </div>
            <div class="hero-desc">
                Explore trailers in a large cinematic popup, jump into a full detail page,
                and browse movies through a polished Netflix, Prime Video, and Hotstar inspired interface.
            </div>
            <div class="hero-meta-row">
                <span class="meta-chip">⭐ {featured['rating']}</span>
                <span class="meta-chip">{featured['genre']}</span>
                <span class="meta-chip">{featured['year']}</span>
                <span class="meta-chip">{featured['duration']}</span>
                <span class="meta-chip">{featured['language']}</span>
            </div>
        </div>
        <div class="hero-poster-card">
    </div>
</div>
""", unsafe_allow_html=True)

col_a, col_b, col_c, col_d = st.columns([1.15, 1.15, 1, 1])
with col_a:
    if st.button("▶ Play Trailer Popup", key="hero_popup"):
        show_trailer_popup(featured)
with col_b:
    if st.button("📺 Open Full Detail Page", key="hero_page"):
        set_selected_movie(featured.to_dict())
        st.switch_page("pages/7_Trailer_Player.py")
with col_c:
    if st.button("⬅ Previous", key="hero_prev"):
        prev_feature(len(df))
        st.rerun()
with col_d:
    if st.button("Next ➜", key="hero_next"):
        next_feature(len(df))
        st.rerun()

st.image(featured["image"], use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

section_header("Trending Now", "Quick-play posters with popup and full page options")
st.markdown('<div class="rail-wrap">', unsafe_allow_html=True)

clicked = clickable_images(
    df["image"].tolist(),
    titles=[f"{row['title']} ({row['year']})" for _, row in df.iterrows()],
    div_style={
        "display": "flex",
        "justify-content": "flex-start",
        "flex-wrap": "wrap",
        "gap": "14px"
    },
    img_style={
        "height": "280px",
        "border-radius": "18px",
        "cursor": "pointer",
        "box-shadow": "0 12px 25px rgba(0,0,0,0.30)",
        "border": "1px solid rgba(255,255,255,0.08)"
    },
    key="premium_poster_row"
)

if clicked > -1:
    show_trailer_popup(df.iloc[clicked])

st.markdown('</div>', unsafe_allow_html=True)

section_header("Curated Grid", "Use popup for fast preview or open a dedicated detail page")
cols = st.columns(4)

for i in range(min(len(df), 8)):
    row = df.iloc[i]
    with cols[i % 4]:
        st.markdown('<div class="poster-card">', unsafe_allow_html=True)
        st.image(row["image"], use_container_width=True)
        st.markdown(f"""
        <div class="poster-meta">
            <div class="poster-title">{row['title']}</div>
            <div class="poster-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button(f"▶ Popup - {row['title']}", key=f"grid_pop_{i}"):
            show_trailer_popup(row)

        if st.button(f"📺 Detail - {row['title']}", key=f"grid_page_{i}"):
            set_selected_movie(row.to_dict())
            st.switch_page("pages/7_Trailer_Player.py")
