from __future__ import print_function
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

#Input Spotify username below
username = ''


#Spotify authentication reading from json file. Hard code these values if you want
#These values are from the spotify developer dashboard

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

#Adds spotify tracks to playlist using spotipy queries from xml parse
def Mp3_to_Spotify(mp3_dict, playlistID):
    track_URLs = []
    count = 10
    for entry in mp3_dict:
        title = entry['Name']
        artist = entry['Artist']
        album = entry['Album']
        year = entry['Year']

        query = title + ' ' + artist
        search_result = sp.search(query, limit=1, offset=0, type='track')
        
        
        if search_result['tracks']['items']:
            track_URLs.append(search_result['tracks']['items'][0]['id'])
        if count == 0:
            break
        count = count - 1

    print(track_URLs)
    sp.user_playlist_add_tracks(username, playlistID, track_URLs)
    return

#Gets playlist tracks from spotify playlist
def get_playlist_tracks(playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

#Cleans spotify track titles
def clean_spotify_tracks(tracks):
    tracks_cleaned = []
    for track in tracks:
        album = track['track']['album']['name']
        artist = track['track']['album']['artists'][0]['name']
        track = track['track']['name']
        tracks_cleaned.append(artist + " - " + track + " - " + album)
    return tracks_cleaned

#Adds tracks to youtube playlist using spotify track titles
def youtube_to_spotify(song_list, playlistID):
    track_URLs = []
    count = 10
    for entry in song_list:
        search_result = sp.search(entry, limit=1, offset=0, type='track')
        if search_result['tracks']['items']:
            track_URLs.append(search_result['tracks']['items'][0]['id'])
        if count == 0:
            break
        count = count - 1

    sp.user_playlist_add_tracks(username, playlistID, track_URLs)
    return