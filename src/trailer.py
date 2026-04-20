import requests

def get_trailer(movie):
    api_key = "YOUR_YOUTUBE_API_KEY"

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie}+trailer&key={api_key}&maxResults=1"

    response = requests.get(url)
    data = response.json()

    try:
        video_id = data["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    except:
        return None