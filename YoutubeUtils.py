from __future__ import print_function
from ytmusicapi import YTMusic

#create ytmusic oauth file before running this!
ytmusic = YTMusic("oauth.json")

#Adds tracks to youtube playlist
def add_songs_to_playlist(tracks_cleaned, playlist_id):
    song_ids = []
    for track in tracks_cleaned:
        song = ytmusic.search(query = track, filter = 'songs', limit=1)
        song_ids.append(song[0]['videoId'])
    
    print(song_ids)
    ytmusic.add_playlist_items(playlistId=playlist_id, videoIds=song_ids)

#Gets track titles from youtube playlist
def get_songs_from_ytplaylist(playlistId, number_of_tracks):
    song_list = []
    songs = ytmusic.get_playlist(playlistId= playlistId)
    
    for i in range(number_of_tracks):
        title = songs['tracks'][i]['title']
        artist = songs['tracks'][i]['artists'][0]['name']
        song_list.append(title + " " + artist)

    songs = ytmusic.get_playlist(playlistId= playlistId)
    return song_list