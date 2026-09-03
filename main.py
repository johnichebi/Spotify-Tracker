import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from pathlib import Path
import requests
import groq
import dotenv
import json
import os

BASE_DIR = Path(__file__).parent
dotenv.load_dotenv(BASE_DIR / ".env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

print("Client ID loaded:", CLIENT_ID is not None)
print("Client secret loaded:", CLIENT_SECRET is not None)

CACHE_PATH = BASE_DIR / ".spotify_cache"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8080/callback",
    scope="user-read-recently-played user-top-read user-read-currently-playing user-read-playback-state",
    cache_path=str(BASE_DIR / ".spotify_cache"),
    open_browser=False
))

