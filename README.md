This repo contains tools to migrate MP3 .xml files to Spotify/Youtube playlists and Spotify/Youtube playlists to each other.

Spotipy is used for the Spotify integration and ytmusicapi for the Youtube Music integration.

In order to migrate your mp3 playlists you need to alter the path to wherever your .xml file is located.

Spotify requires a developer account (free and simple to create). You then need to create an App on the dashboard and find the client id and localhost.
Put in these values to the SpotifyAuth.json file.

Youtube Music also requires using the developer dashboard. You must create an oauth token and path to it in the code.

When migrating between Spotify and Youtube, you need to change the 'count' variable to the number of tracks you want to migrate. 
Also input your Spotify/Youtube playlist ids.



