import streamlit as st
import pandas as pd

st.title("🔤 Movie Recommender (First Letter Based)")

# Load dataset
df = pd.read_csv("data/movies.csv")

# make sure column exists
if "title" in df.columns:
    movies = df["title"].dropna().tolist()
else:
    movies = ["Inception", "Interstellar", "Avatar", "Titanic", "Avengers"]

# Input box
letter = st.text_input("Enter first letter of movie (A-Z)").lower()

def recommend_by_letter(l):
    results = [m for m in movies if m.lower().startswith(l)]
    return results

# Button
if st.button("Ask Ai") and letter:
    results = recommend_by_letter(letter)

    if results:
        st.success("Recommended Movies 🎬")
        for r in results:
            st.write("👉", r)
    else:
        st.warning("No movies found for this letter 😢")