import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")
    df["overview"] = df["overview"].fillna("")
    df["genre"] = df["genre"].fillna("")
    df["content"] = df["overview"] + " " + df["genre"]
    return df

def get_recommendations(title):
    df = load_data()

    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(df["content"])
    similarity = cosine_similarity(matrix)

    if title not in df["title"].values:
        return []

    idx = df[df["title"] == title].index[0]

    scores = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)

    return [df.iloc[i[0]] for i in scores[1:6]]