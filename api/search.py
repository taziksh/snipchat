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
    def search(self, phrase):
        """ Return tracks that match keywords in given phrase. """
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.config['SPOTIFY_CLIENT_ID'], client_secret=self.config['SPOTIFY_CLIENT_SECRET']))
        results = spotify.search(q=phrase, type='track', limit=5)
        tracks = [track['name'] for idx, track in enumerate(results['tracks']['items'])]
        return tracks

class YouTubeSearch(Search):
    def search(self, track):
        videos = VideosSearch(track.lower(), limit=3)
        return videos.result()['result'][0]['id']
