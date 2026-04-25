import streamlit as st
from src.recommender import (
    load_data,
    get_recommendations,
    get_mood_recommendations,
    get_mood_mapping
)
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session, add_to_watchlist, set_selected_movie

st.set_page_config(
    page_title="AI Recommender | OTT Stream Pro Max",
    page_icon="🤖",
    layout="wide"
)

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">MOOD AI</span>
        <span class="hero-pill">SMART DISCOVERY</span>
        <span class="hero-pill">OTT STYLE</span>
    </div>
    <div class="hero-title">
        Pick your <span class="accent">mood</span> and discover your next movie
    </div>
    <div class="hero-desc">
        Mee current mood, vibe, or favorite movie batti quick ga recommendations pondandi.
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["😊 Mood Based", "🎬 Title Based"])

with tab1:
    section_header("Mood Matcher", "Mee mood select chesthe matching movies chupisthundi")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        moods = list(get_mood_mapping().keys())
        selected_mood = st.selectbox("Select your mood", moods)

    with col2:
        count = st.slider("How many recommendations?", 4, 12, 8)

    mood_recs = get_mood_recommendations(selected_mood, count)

    st.markdown(
        f"""
        <div class="section-sub">
            Showing movies for <b>{selected_mood}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(4, gap="large")
    for i, (_, row) in enumerate(mood_recs.iterrows()):
        with cols[i % 4]:
            st.markdown('<div class="grid-card">', unsafe_allow_html=True)
            st.image(row["image"], width="stretch")
            st.markdown(f"""
                <div class="movie-title">{row['title']}</div>
                <div class="movie-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
                <div style="color:#9aa8c3;font-size:0.88rem;line-height:1.6;">
                    {row['overview']}
                </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            with c1:
                if st.button("❤️ Watchlist", key=f"mood_watch_{i}"):
                    if add_to_watchlist(row["title"]):
                        st.success(f"{row['title']} added")
                    else:
                        st.info("Already added")
            with c2:
                if st.button("📺 Open", key=f"mood_open_{i}"):
                    set_selected_movie(row.to_dict())
                    st.switch_page("pages/7_Trailer_Player.py")

with tab2:
    section_header("Movie Similarity", "Mee favorite movie select chesthe similar titles suggest chesthundi")

    selected_title = st.selectbox("Choose a movie", df["title"].tolist())
    top_n = st.slider("Recommendations count", 4, 12, 6, key="title_slider")

    if st.button("✨ Recommend Similar Movies"):
        recs = get_recommendations(selected_title, top_n)

        if recs.empty:
            st.warning("No recommendations found.")
        else:
            st.success(f"Movies similar to {selected_title}")

            cols = st.columns(3, gap="large")
            for i, (_, row) in enumerate(recs.iterrows()):
                with cols[i % 3]:
                    st.markdown('<div class="grid-card">', unsafe_allow_html=True)
                    st.image(row["image"], width="stretch")
                    st.markdown(f"""
                        <div class="movie-title">{row['title']}</div>
                        <div class="movie-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
                        <div style="color:#9aa8c3;font-size:0.88rem;line-height:1.6;">
                            {row['overview']}
                        </div>
                    """, unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    c1, c2 = st.columns(2)
                    with c1:
                        if st.button("❤️ Watchlist", key=f"title_watch_{i}"):
                            if add_to_watchlist(row["title"]):
                                st.success(f"{row['title']} added")
                            else:
                                st.info("Already added")
                    with c2:
                        if st.button("📺 Open", key=f"title_open_{i}"):
                            set_selected_movie(row.to_dict())
                            st.switch_page("pages/7_Trailer_Player.py")
