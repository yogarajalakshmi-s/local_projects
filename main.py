import os
import requests
from bs4 import BeautifulSoup
import spotipy  # https://spotipy.readthedocs.io/en/2.13.0/#ids-uris-and-urls
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI') # here you need to put the same URI in your Spotify account
SCOPE = "playlist-modify-private"

date = input("Which day would you like to travel to? (YYYY-MM-DD): ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
website_html = response.text

# Get data from billboard
soup = BeautifulSoup(website_html, "html.parser")
songs = []
first_song = (soup.find(name="h3", class_="c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color"
"-black u-color-white@mobile-max lrv-u-margin-r-150")).getText().strip()
remaining_songs = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size"
"-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max "
"a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
songs = [song.getText().strip() for song in remaining_songs]
songs.insert(0, first_song)

# Search Spotify to get the URIs
sp = spotipy.Spotify(auth_manager=SpotifyOAuth
            (
                scope=SCOPE,
                redirect_uri =SPOTIPY_REDIRECT_URI,
                client_id =SPOTIPY_CLIENT_ID,
                client_secret = SPOTIPY_CLIENT_SECRET,
                show_dialog = True,
                cache_path = "token.txt",
            )
        )

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
        # print(f"{song} doesn't exist in Spotify. Skipped.")
    # print(result)

# Create a private Spotify playlist
user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
