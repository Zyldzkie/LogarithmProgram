# pip install spotipy first

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import csv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

# the target playlist
playlist_id = '0lwLW6fgeiTzNV7wCoMR7V'

def get_all_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks


all_tracks = get_all_playlist_tracks(playlist_id)

sorted_tracks = sorted(all_tracks, key=lambda x: x['track']['name'])


csv_filename = 'song_name.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Track Name'])  
    for item in sorted_tracks:
        track = item['track']
        writer.writerow([track['name']]) 

