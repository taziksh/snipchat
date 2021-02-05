import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import yaml

config = None
with open('config.yml', 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exception:
        raise exception("Could not load config.yml")

def search(phrase):
    """ Return tracks that match keywords in given phrase. """
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config['SPOTIFY_CLIENT_ID'], client_secret=config['SPOTIFY_CLIENT_SECRET']))
    results = spotify.search(q=phrase, type='track', limit=5)
    tracks = [track['name'] for idx, track in enumerate(results['tracks']['items'])]
    #TODO: compare results, possibly based on additional info from frontend
    #TODO: return track['duration_ms], track['album']['artists']
    return tracks[0]
