import sys
import spotipy
import spotipy.util as util
'''
scope = 'user-library-read'
username = '22jk5kjdeaqulvfeky5y2nxpa'
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)
'''


token=util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)


lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(auth=token)
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print ('track    : ' + track['name'])
    print ('audio    : ' + track['preview_url'])
    print ('cover art: ' + track['album']['images'][0]['url'])
    print ()

