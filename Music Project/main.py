import sys
import spotipy
import spotipy.util as util

username='22jk5kjdeaqulvfeky5y2nxpa'
scope='user-library-read'
client_id='40f479d045e74be1bbf1baf5da1a5dc8'
client_secret='e88bd4ecc08c4bb080ba87ae23bf01c1'
redirect_uri='http://localhost/'

token=util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)


lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(auth=token)
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print ('track    : ' + track['name'])
    print ('audio    : ' + track['preview_url'])
    print ('cover art: ' + track['album']['images'][0]['url'])
    print ()

