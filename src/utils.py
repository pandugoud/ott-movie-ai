import requests
import streamlit as st


def initialize_session():
    if "watchlist" not in st.session_state:
        st.session_state.watchlist = []
    if "theme_label" not in st.session_state:
        st.session_state.theme_label = "Dark"


def add_to_watchlist(movie_name):
    if movie_name and movie_name not in st.session_state.watchlist:
        st.session_state.watchlist.append(movie_name)
        return True
    return False


def remove_from_watchlist(movie_name):
    if movie_name in st.session_state.watchlist:
        st.session_state.watchlist.remove(movie_name)
        return True
    return False


def get_trailer(movie):
    api_key = "YOUR_YOUTUBE_API_KEY"
    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={movie}+official+trailer&key={api_key}&maxResults=1"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        video_id = data["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    except Exception:
        return None
