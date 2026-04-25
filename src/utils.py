import streamlit as st


def initialize_session():
    defaults = {
        "watchlist": [],
        "selected_movie": None,
        "featured_index": 0,
        "now_playing": None,
        "player_open": False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


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


def set_selected_movie(movie_dict):
    st.session_state.selected_movie = movie_dict


def next_feature(total):
    st.session_state.featured_index = (st.session_state.featured_index + 1) % total


def prev_feature(total):
    st.session_state.featured_index = (st.session_state.featured_index - 1) % total


def play_movie(movie):
    st.session_state.now_playing = movie
    st.session_state.player_open = True


def stop_movie():
    st.session_state.now_playing = None
    st.session_state.player_open = False


def is_playing(movie=None):
    if not st.session_state.get("player_open", False):
        return False

    current = st.session_state.get("now_playing", None)

    if movie is None:
        return current is not None

    if isinstance(movie, dict) and isinstance(current, dict):
        return current.get("title") == movie.get("title")

    return current == movie
