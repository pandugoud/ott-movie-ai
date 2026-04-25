# OTT Stream Pro Max

A premium multipage Streamlit movie discovery app with OTT-style UI, smart recommendations, watchlist support, and trailer viewing. The app structure follows Streamlit's multipage `pages/` directory approach, and navigation between pages can be handled with `st.switch_page()` in supported versions.[1][2]

## Features

- Premium dark OTT-inspired interface with shared styling across all pages.
- Multipage structure for Home, Explore, AI Recommender, Watchlist, Trailer Player, Analytics, and About Us.
- Mood-based movie recommendations.
- Title-based similar movie recommendations using TF-IDF and cosine similarity.
- Movie search by title, genre, language, year, or overview.
- Watchlist using Streamlit session state.
- Trailer viewing page with selected movie details.
- Reusable shared UI helpers from `src/ui.py`.

## Project Structure

```text
ott-movie-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── data/
│   └── movies.csv
├── src/
│   ├── __init__.py
│   ├── recommender.py
│   ├── ui.py
│   └── utils.py
└── pages/
    ├── 1_Home.py
    ├── 2_Explore.py
    ├── 3_AI_Recommender.py
    ├── 4_About_Us.py
    ├── 5_Watchlist.py
    ├── 6_Analytics.py
    └── 7_Trailer_Player.py
```

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Recommended `requirements.txt`:

```txt
streamlit
pandas
scikit-learn
requests
```

## Run Locally

Start the app with:

```bash
streamlit run app.py
```

Streamlit supports multipage apps through the `pages/` directory, so every file in that folder becomes a page automatically.[1]

## Configuration

Example `.streamlit/config.toml`:

```toml
[theme]
base="dark"
primaryColor="#2a9d8f"
backgroundColor="#08131f"
secondaryBackgroundColor="#10202f"
textColor="#edf6f9"
font="sans serif"
baseRadius="large"
borderColor="#213547"
showWidgetBorder=true
```

`st.set_page_config()` should be called at the top of each page before other Streamlit commands to control title, icon, and layout.[3]

## Main Pages

### Home

The Home page acts as the premium landing screen for the app. It can show featured content, top picks, and quick navigation actions.

### Explore

The Explore page allows searching across the movie dataset using title, genre, overview, language, and year.

### AI Recommender

This page provides two recommendation flows:

- Mood-based suggestions.
- Title-based similar recommendations.

The recommendation engine uses TF-IDF vectorization and cosine similarity to find related titles from the dataset.

### About Us

The About Us page explains the platform, mission, vision, and core offerings in the same shared UI style as the rest of the app.

### Watchlist

The Watchlist page reads saved movie titles from session state and lets users remove or open saved titles.

### Trailer Player

The Trailer Player page shows the selected movie poster, details, and embedded trailer link.

### Analytics

The Analytics page can display dataset summaries such as total movies, top genre, and genre counts using `load_data()` and `get_genre_counts()`.

## Shared Modules

### `src/recommender.py`

Contains:

- `load_data()`
- `build_similarity()`
- `search_movies()`
- `get_recommendations()`
- `get_movie_by_title()`
- `get_genre_counts()`
- `get_mood_mapping()`
- `get_mood_recommendations()`

If `pages/6_Analytics.py` imports `get_genre_counts`, that function must exist in `src/recommender.py`; otherwise Python raises an import error for the missing name.[4]

### `src/utils.py`

Handles shared session state:

- Watchlist storage
- Selected movie state
- Featured movie index

Session state is useful for preserving values across user interaction in a Streamlit app.[1]

### `src/ui.py`

Contains shared CSS and layout helpers such as:

- `inject_css()`
- `render_sidebar()`
- `topbar()`
- `section_header()`

Using shared UI helpers helps keep button size, layout, and theme styling consistent across multiple pages.

## Button Consistency Pattern

To keep button sizes consistent across all pages:

- Use shared CSS in `src/ui.py`.
- Use equal `st.columns(...)` for button rows.
- Use `st.button(..., width="stretch")` for full-width buttons inside each column, as supported by Streamlit button configuration.[5]

Example:

```python
c1, c2 = st.columns(2, gap="small")
with c1:
    if st.button("❤️ Watchlist", key="watch_1", width="stretch"):
        pass
with c2:
    if st.button("📺 Open", key="open_1", width="stretch"):
        pass
```

## Navigation Pattern

To move from one page to another inside the multipage app, use `st.switch_page()` with a valid page path.[2]

Example:

```python
if st.button("ℹ️ About Us", width="stretch"):
    st.switch_page("pages/4_About_Us.py")
```

## Fix for Analytics Import Error

If the app shows this error:

```python
from src.recommender import load_data, get_genre_counts
```

and `get_genre_counts` is missing, add this function inside `src/recommender.py`:

```python
def get_genre_counts():
    df = load_data()
    return df["genre"].value_counts()
```

This resolves the missing import issue caused by trying to import a function that is not defined in the module.[4][6]

## Sample Analytics Page

```python
import streamlit as st
from src.recommender import load_data, get_genre_counts
from src.ui import inject_css, render_sidebar, topbar, section_header
from src.utils import initialize_session

st.set_page_config(page_title="Analytics | OTT Stream Pro Max", page_icon="📊", layout="wide")

initialize_session()
inject_css()
render_sidebar()
topbar()

section_header("Analytics", "Movie dataset overview")

df = load_data()
genre_counts = get_genre_counts()

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Total Movies", len(df))
with c2:
    st.metric("Total Genres", genre_counts.shape[0])
with c3:
    st.metric("Top Genre", genre_counts.index[0] if len(genre_counts) else "N/A")

st.subheader("Genre Counts")
st.bar_chart(genre_counts)
```

## Deployment

This app can be deployed to Streamlit Community Cloud or any environment that supports Streamlit. If deploying on Streamlit Cloud, dependency and import issues can be checked from the app logs in the management interface when runtime errors occur.[7]

## Future Improvements

- TMDB API integration for live movie data.
- User authentication.
- Personalized recommendation history.
- Real OTT availability lookup.
- Better analytics and charts.
- Contact Us page and feedback form.

## License

This project can be used as a learning project, portfolio project, or base template for a movie recommendation app.
