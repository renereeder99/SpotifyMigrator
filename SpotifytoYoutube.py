from __future__ import print_function
import spotipy
import xml.etree.ElementTree as ET
from spotipy.oauth2 import SpotifyOAuth
import json
from ytmusicapi import YTMusic
from SpotifyUtils import get_playlist_tracks, clean_spotify_tracks
from YoutubeUtils import add_songs_to_playlist

#youtube music and spotify authentication
#create ytmusic oauth file before running this!
ytmusic = YTMusic("oauth.json")

#Put in Spotify username below
username = ''

#Spotify authentication reading from json file. Hard code these values if you want
with open ('SpotifyAuth.json', 'r') as file:
    SpAuth = json.load(file)

client_id = SpAuth['client_id']
client_secret = SpAuth['client_id']
redirect_uri = SpAuth['client_id']
scope = SpAuth['client_id']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope= scope))

#Input your spotify and youtube playlist ids
spotify_playlist_id = ''
youtube_playlist_id = ''

#Get and clean spotify track titles
spotify_tracks = get_playlist_tracks(spotify_playlist_id)
spotify_tracks_cleaned = clean_spotify_tracks(spotify_tracks)

#Add songs to youtube playlist with youtube playlistid
add_songs_to_playlist(spotify_tracks_cleaned, youtube_playlist_id)



        
   






