import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("data/movies.csv")

st.markdown("""
<div style="background:#000;padding:40px;border-radius:10px;">
<h1 style="color:white;">Unlimited Movies & AI Recommendations</h1>
</div>
""", unsafe_allow_html=True)

st.subheader("🔥 Trending Now")

cols = st.columns(4)

for i in range(min(4, len(df))):
    with cols[i]:
        st.image(df.iloc[i]["image"], use_container_width=True)
        st.caption(df.iloc[i]["title"])