import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

CLIENTID = "e144e8004f944145b39884166551639b"
CLIENTSECRET = "28f12fb93fbf455aab727b4f31027ce9"
REDIRECTURL = "https://example.com/callback"
SCOPE = "playlist-modify-private"
URL = "https://www.billboard.com/charts/hot-100/2000-08-12"  # Example date

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENTID,
    client_secret=CLIENTSECRET,
    redirect_uri=REDIRECTURL,
    scope=SCOPE
))

# Get the authenticated user's ID
user_info = sp.current_user()
user_id = user_info['id']  # This is the user ID we will use for playlist creation

# Send a request to Billboard to scrape the song names
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

billboard_response = requests.get(URL, headers=header)
soup = BeautifulSoup(billboard_response.text, "html.parser")

# Extract song titles from the Billboard page
all_songs = soup.select("ul li h3#title-of-a-story")
songs = [_.get_text(strip=True) for _ in all_songs]

# Create a new playlist with the specified name
playlist_name = "2000-08-12 Billboard 100"
new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False)

# Now, let's add the songs to the new playlist by searching for each song's URI
track_uris = []
for song in songs:
    result = sp.search(q=song, type="track", limit=1)
    if result['tracks']['items']:
        track_uri = result['tracks']['items'][0]['uri']
        track_uris.append(track_uri)
    else:
        print(f"Track not found: {song}")

# Add all found tracks to the new playlist
if track_uris:
    sp.playlist_add_items(new_playlist['id'], track_uris)

# Print playlist details
pprint.pprint(new_playlist)
