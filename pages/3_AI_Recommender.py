import streamlit as st
from src.recommender import load_data, get_recommendations, get_mood_recommendations, get_mood_mapping
from src.ui import inject_css, render_sidebar, topbar, section_header, poster_image
from src.utils import initialize_session, add_to_watchlist, set_selected_movie

st.set_page_config(page_title="AI Recommender | OTT Stream Pro Max", page_icon="🤖", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

df = load_data()

st.markdown("""
<div class="hero-v2">
    <div class="hero-pills">
        <span class="hero-pill">AI RECOMMENDER</span>
        <span class="hero-pill">MOOD AI</span>
        <span class="hero-pill">SIMILARITY ENGINE</span>
    </div>
    <div class="hero-title">
        Find smarter picks with <span class="accent">AI-style recommendations</span>
    </div>
    <div class="hero-desc">
        Choose by mood or start from a movie you already love and discover related titles quickly.
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["😊 Mood Based", "🎬 Title Based"])

with tab1:
    section_header("Mood Matcher", "Select your vibe")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        moods = list(get_mood_mapping().keys())
        selected_mood = st.selectbox("Select your mood", moods)
    with col2:
        count = st.slider("How many recommendations?", 4, 12, 8)

    mood_recs = get_mood_recommendations(selected_mood, count)

    cols = st.columns(4, gap="large")
    for i, (_, row) in enumerate(mood_recs.iterrows()):
        with cols[i % 4]:
            st.markdown('<div class="grid-card">', unsafe_allow_html=True)
            poster_image(row["image"])
            st.markdown(f"""
                <div class="movie-title">{row['title']}</div>
                <div class="movie-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
                <div style="color:#91a4b7;font-size:0.88rem;line-height:1.72;">{row['overview']}</div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            c1, c2 = st.columns(2, gap="small")
            with c1:
                if st.button("❤️ Watchlist", key=f"mood_watch_{i}", width="stretch"):
                    if add_to_watchlist(row["title"]):
                        st.success("Added")
                    else:
                        st.info("Already added")
            with c2:
                if st.button("📺 Open", key=f"mood_open_{i}", width="stretch"):
                    set_selected_movie(row.to_dict())
                    st.switch_page("pages/7_Trailer_Player.py")

with tab2:
    section_header("Movie Similarity", "Choose a favorite title")
    t1, t2 = st.columns(2, gap="large")
    with t1:
        selected_title = st.selectbox("Choose a movie", df["title"].tolist())
    with t2:
        top_n = st.slider("Recommendations count", 4, 12, 6, key="title_slider")

    if st.button("✨ Recommend Similar Movies", key="recommend_similar", width="stretch"):
        recs = get_recommendations(selected_title, top_n)

        if recs.empty:
            st.warning("No recommendations found.")
        else:
            cols = st.columns(3, gap="large")
            for i, (_, row) in enumerate(recs.iterrows()):
                with cols[i % 3]:
                    st.markdown('<div class="grid-card">', unsafe_allow_html=True)
                    poster_image(row["image"])
                    st.markdown(f"""
                        <div class="movie-title">{row['title']}</div>
                        <div class="movie-sub">{row['genre']} • {row['year']} • ⭐ {row['rating']}</div>
                        <div style="color:#91a4b7;font-size:0.88rem;line-height:1.72;">{row['overview']}</div>
                    """, unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    c1, c2 = st.columns(2, gap="small")
                    with c1:
                        if st.button("❤️ Watchlist", key=f"title_watch_{i}", width="stretch"):
                            if add_to_watchlist(row["title"]):
                                st.success("Added")
                            else:
                                st.info("Already added")
                    with c2:
                        if st.button("📺 Open", key=f"title_open_{i}", width="stretch"):
                            set_selected_movie(row.to_dict())
                            st.switch_page("pages/7_Trailer_Player.py")
