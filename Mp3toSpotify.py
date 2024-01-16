from __future__ import print_function
import spotipy
import json
import xml.etree.ElementTree as ET
from spotipy.oauth2 import SpotifyOAuth
from SpotifyUtils import Mp3_to_Spotify
from Mp3Utils import extract_data_from_dict, mp3_list_to_dictionary, mp3_list_to_query

#youtube music and spotify authentication
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

#Replace with your path to .xml
path = 'SpotifyMigrator\iTunes Music Library.xml'

#Replace with your spotify playlist id
spotify_playlist_id = ''

#Parses xml file and creates a dictionary to query spotipy
result_info = mp3_list_to_dictionary(path)
query = mp3_list_to_query(result_info)

#Creates a spotify playlist with queries from xml
Mp3_to_Spotify(result_info, spotify_playlist_id)



