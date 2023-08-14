from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Getting list from 100 best songs
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2000-08-12"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select("div.o-chart-results-list-row-container ul li ul li h3#title-of-a-story")
song_names = [song.getText().strip() for song in titles]
print(song_names)


# Init api spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt",
        username="",
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2000-08-12"

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
