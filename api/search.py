from abc import ABC, abstractmethod 

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml

from youtubesearchpython import VideosSearch

class Search(ABC):
    @abstractmethod
    def search(self, input):
        pass

class SpotifySearch(Search):
    def __init__(self):
        config = None
        with open('config.yml', 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exception:
                raise exception("Could not load config.yml")

    #TODO: compare results, possibly based on additional info from frontend
    #TODO: return track['duration_ms], track['album']['artists']
    def search(self, query):
        """ Return tracks that match keywords in given query. """
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.config['SPOTIFY_CLIENT_ID'], client_secret=self.config['SPOTIFY_CLIENT_SECRET']))
        response = spotify.search(q=query, type='track', limit=5)
        #TODO: only returning first result...?
        results = ()
        for i, track in enumerate(response['tracks']['items']):
            results = results + (track['name'], track['duration_ms'])
        return results 

class YouTubeSearch(Search):
    def search(self, track):
        videos = VideosSearch(track.lower(), limit=3)
        return videos.result()['result'][0]['id']
