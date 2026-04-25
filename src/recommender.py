import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")

    required_cols = [
        "title", "overview", "genre", "image", "trailer",
        "year", "duration", "language", "rating"
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    df = df.fillna("")

    for col in required_cols:
        df[col] = df[col].astype(str)

    df["content"] = (
        df["title"] + " " +
        df["overview"] + " " +
        df["genre"] + " " +
        df["language"]
    )

    return df


@st.cache_data
def build_similarity():
    df = load_data()
    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(df["content"])
    similarity = cosine_similarity(matrix)
    return similarity


def search_movies(query):
    df = load_data()

    if not query or str(query).strip() == "":
        return df

    q = str(query).strip()

    results = df[
        df["title"].str.contains(q, case=False, na=False) |
        df["genre"].str.contains(q, case=False, na=False) |
        df["overview"].str.contains(q, case=False, na=False) |
        df["language"].str.contains(q, case=False, na=False) |
        df["year"].str.contains(q, case=False, na=False)
    ].copy()

    return results


def get_recommendations(title, top_n=6):
    df = load_data()
    similarity = build_similarity()

    if title not in df["title"].values:
        return pd.DataFrame()

    idx = df.index[df["title"] == title][0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    filtered = [x for x in scores if x[0] != idx][:top_n]
    indices = [x[0] for x in filtered]

    return df.iloc[indices].copy()


def get_movie_by_title(title):
    df = load_data()
    matched = df[df["title"] == title]

    if matched.empty:
        return None

    return matched.iloc[0].to_dict()


def get_mood_mapping():
    return {
        "😊 Happy": ["Comedy", "Romance", "Animation", "Fantasy", "Music", "Family"],
        "😌 Relaxed": ["Drama", "Romance", "Family", "Fantasy"],
        "🔥 Excited": ["Action", "Adventure", "Sci-Fi", "Thriller"],
        "🤯 Mind-Bending": ["Sci-Fi", "Mystery", "Thriller"],
        "😢 Emotional": ["Drama", "Romance"],
        "😎 Mass / Hero Vibe": ["Action", "Adventure"],
        "🌌 Escapist": ["Fantasy", "Sci-Fi", "Adventure"],
        "🇮🇳 Telugu Vibe": ["Action", "Drama"]
    }


def get_mood_recommendations(mood, top_n=8):
    df = load_data()
    mood_map = get_mood_mapping()

    if mood not in mood_map:
        return df.head(top_n).copy()

    target_genres = mood_map[mood]

    filtered = df[
        df["genre"].apply(
            lambda x: any(g.lower() in str(x).lower() for g in target_genres)
        )
    ].copy()

    if filtered.empty:
        return df.head(top_n).copy()

    filtered["rating_num"] = pd.to_numeric(filtered["rating"], errors="coerce").fillna(0)
    filtered = filtered.sort_values(by="rating_num", ascending=False)

    return filtered.head(top_n).copy()
