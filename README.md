# Spotify Playlist

Created a private Spotify playlist by scraping data from billboard.
The date will be given as input and the top 100 songs from that date will be created as a private playlist in our Spotify account

**Tech Stack** - Python, BeautifulSoup, Spotipy 

**1. Created a Spotify Developer Account**  
  - Signed up on Spotify Developers
  - Goto Dashboards -> Created a new App
  - In the app settings, added the REDIRECT_URI as http://127.0.0.1:8080/
  - Stored the spotify client ID, client secret, Redirect URI in environment variables.

**2. Get the songs from Billboard**  
  - Scraped html data using BeautifulSoup from Billboard for the input date

**3. Search through Spotify to get the song URI**  
  - Created Spotipy object with the required credentials.
  - Searched the songs through the URI, skipped if the song doesn't exist and stored them all.

**4. Creating playlist**  
  - Created a playlist under the current user.
  - Added the stored songs to this playlist.

**Reference**  
https://spotipy.readthedocs.io/en/2.13.0/
