from __future__ import print_function
import json
import spotipy
import xml.etree.ElementTree as ET
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy.util
from ytmusicapi import YTMusic
from SpotifyUtils import youtube_to_spotify
from YoutubeUtils import get_songs_from_ytplaylist

#youtube music and spotify authentication
#create ytmusic oauth file before running this
ytmusic = YTMusic("oauth.json")

#Input spotify username below
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
num_of_tracks = 25

#Get songs from youtube playlist
song_list = get_songs_from_ytplaylist(playlistId=youtube_playlist_id, number_of_tracks=num_of_tracks)

#Add songs to spotify playlist with spotify playlistid
youtube_to_spotify(song_list, spotify_playlist_id, username)


