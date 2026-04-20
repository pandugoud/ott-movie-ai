import streamlit as st

st.title("❤️ Watchlist")

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

movie = st.text_input("Add Movie")

if st.button("Add"):
    st.session_state.watchlist.append(movie)

st.write("Your Watchlist:")

for m in st.session_state.watchlist:
    st.write("🎬", m)