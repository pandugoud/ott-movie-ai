import streamlit as st
import pandas as pd

st.title("🔎 Explore Movies")

df = pd.read_csv("data/movies.csv")

search = st.text_input("Search Movies")

filtered = df[df["title"].str.contains(search, case=False)] if search else df

cols = st.columns(3)

for i in range(len(filtered)):
    with cols[i % 3]:
        st.image(filtered.iloc[i]["image"], use_container_width=True)
        st.caption(filtered.iloc[i]["title"])