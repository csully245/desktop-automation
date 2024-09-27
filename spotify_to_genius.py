import requests
from bs4 import BeautifulSoup

def spotify_to_genius(url_spotify):

    # Get title from Spotify
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    title_spotify = soup.find_all('title')[0].get_text()

    # Turn into Genius URL
    title_split = title_spotify.split(" - song by ")
    song_title = title_split[0]
    artist = title_split[1].split(" | Spotify")[0]
    url_genius = "https://genius.com/" + artist + "-" + song_title + "-lyrics"
    url_genius = url_genius.replace(" ", "-")
    return url_genius

if __name__ == "__main__":
    url = input("URL?\n")
    print(spotify_to_genius(url))