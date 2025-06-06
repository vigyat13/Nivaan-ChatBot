import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


SPOTIPY_CLIENT_ID = 'SPOTIPY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'SPOTIPY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # use with ngrok if needed

scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

auth_manager = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope,
    open_browser=True
)

sp = spotipy.Spotify(auth_manager=auth_manager)

def play_spotify_song(song_name):
    results = sp.search(q=song_name, limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        uri = track['uri']
        sp.start_playback(uris=[uri])
    else:
        print("Song not found.")
