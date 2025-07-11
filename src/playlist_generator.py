import requests
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def search_youtube_ost(game_title):
    params = {
        "part": "snippet",
        "q": f"{game_title} OST",
        "type": "video",
        "maxResults": 3,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []

    results = response.json().get("items", [])
    links = [f"https://www.youtube.com/watch?v={item['id']['videoId']}" for item in results]
    return links

def main():
    games = input("Enter your favorite game: ")

    song = search_youtube_ost(games)
    print(song)


if __name__ == "__main__":
    main()