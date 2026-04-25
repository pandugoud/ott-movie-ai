import streamlit as st


def initialize_session():
    defaults = {
        "watchlist": [],
        "playing_movie": None,
        "clicked_movie_title": None
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


def play_movie(title):
    st.session_state.playing_movie = title


def stop_movie():
    st.session_state.playing_movie = None


def is_playing(title):
    return st.session_state.playing_movie == title
