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
        df[col] = df[col].fillna("").astype(str)

    df["content"] = df["overview"] + " " + df["genre"] + " " + df["language"]
    return df


@st.cache_data
def build_similarity():
    df = load_data()
    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(df["content"])
    similarity = cosine_similarity(matrix)
    return similarity


def get_recommendations(title, top_n=6):
    df = load_data()
    similarity = build_similarity()

    if title not in df["title"].values:
        return pd.DataFrame()

    idx = df.index[df["title"] == title][0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    indices = [i[0] for i in scores]
    return df.iloc[indices].copy()


def search_movies(query):
    df = load_data()
    if not query:
        return df

    q = str(query).strip()
    return df[
        df["title"].str.contains(q, case=False, na=False)
        | df["genre"].str.contains(q, case=False, na=False)
        | df["overview"].str.contains(q, case=False, na=False)
        | df["language"].str.contains(q, case=False, na=False)
    ]


def get_genre_counts():
    df = load_data()
    return df["genre"].value_counts()
