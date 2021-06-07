import pysnooper
import os
from abc import ABC, abstractmethod 
import math

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml
from toolz.functoolz import pipe

from youtubesearchpython import VideosSearch

class Search(ABC):
    @abstractmethod
    def search(self, input):
        pass

class SpotifySearch(Search):
    def __init__(self):
        config = None
        rootPath = os.path.abspath(__file__)
        rootDir = os.path.split(rootPath)[0]

        with open('credentials.yml', 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exception:
                raise exception("Could not load config.yml")

    def search(self, query: str):
        """
        :param query: partial lyrics of some track
        :returns: list of top 10 matching tracks 
        """
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.config['SPOTIFY_CLIENT_ID'], client_secret=self.config['SPOTIFY_CLIENT_SECRET']))
        response = spotify.search(q=query, type='track', limit=10)
        results = []
        print('query: ', query)
        for i, track in enumerate(response['tracks']['items']):
            result = (track['name'], track['album']['artists'][0]['name'], track['album']['images'][0]['url'], track['duration_ms'])
            results.append(result)
        print('search results: ', results)
        return results

class YouTubeSearch(Search):
    @pysnooper.snoop()
    def search(self, track: str, spotifyDuration: int) -> str:
        """
        :param track: name of track on Spotify
        :param spotifyDuration: length of track on Spotify
        :returns: id of video on YouTube
        """
        videos = VideosSearch(track.lower(), limit=3)
        mostSimilarPair = ('', math.inf)
        durationSimilarities = []
        for i, video in enumerate(videos.result()['result']):
            id = video['id']
            duration = pipe(video['duration'], self.convertToMillis)
            if abs(duration - spotifyDuration) < mostSimilarPair[1]:
                mostSimilarPair = (id, abs(duration - spotifyDuration))
        return mostSimilarPair[0]

    def convertToMillis(self, time: str) -> int:
      """
      :param time: time as 'mm:ss'  
      :returns: time in milliseconds
      """
      mm, ss = time.split(':')
      mm = int(mm)
      ss = int(mm)
      ms = (mm * 60 + ss) * 1000
      return ms
