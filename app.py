import streamlit as st
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, add_to_watchlist, set_selected_movie
from src.recommender import get_mood_mapping, get_mood_recommendations

st.set_page_config(
    page_title="OTT Stream Pro Max",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_session()
inject_css()
render_sidebar()
topbar()

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">MAIN PAGE MOOD AI</span>
        <span class="hero-pill">QUICK PICKS</span>
        <span class="hero-pill">OTT EXPERIENCE</span>
    </div>
    <div class="hero-title">
        Find movies by your <span class="accent">mood</span>
    </div>
    
</div>
""", unsafe_allow_html=True)

section_header("Mood Based Recommendations")

left, right = st.columns(2, gap="large")
with left:
    moods = list(get_mood_mapping().keys())
    selected_mood = st.selectbox("Choose your mood", moods)
with right:
    rec_count = st.slider("How many movies?", 4, 12, 8)

results = get_mood_recommendations(selected_mood, rec_count)

cols = st.columns(4, gap="large")
for i, (_, row) in enumerate(results.iterrows()):
    with cols[i % 4]:
        st.markdown('<div class="grid-card">', unsafe_allow_html=True)
        st.image(row["image"], width="stretch")
        st.markdown(f"""
            <div class="movie-title">{row['title']}</div>
            <div class="movie-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
            <div style="color:#a7bac7;font-size:0.88rem;line-height:1.6;">{row['overview']}</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        b1, b2 = st.columns(2, gap="small")
        with b1:
            if st.button("❤️ Watchlist", key=f"app_watch_{i}", width="stretch"):
                if add_to_watchlist(row["title"]):
                    st.success("Added")
                else:
                    st.info("Already added")
        with b2:
            if st.button("📺 Open", key=f"app_open_{i}", width="stretch"):
                set_selected_movie(row.to_dict())
                st.switch_page("pages/7_Trailer_Player.py")

section_header("Navigate")
n1, n2, n3 = st.columns(3, gap="small")
with n1:
    if st.button("🔎 Explore", key="nav_explore", width="stretch"):
        st.switch_page("pages/2_Explore.py")
with n2:
    if st.button("🤖 AI Recommender", key="nav_ai", width="stretch"):
        st.switch_page("pages/3_AI_Recommender.py")
with n3:
    if st.button("❤️ Watchlist", key="nav_watchlist", width="stretch"):
        st.switch_page("pages/5_Watchlist.py")
