import pytest

from pprint import pprint

from ..search import SpotifySearch, YouTubeSearch
from ..download import AZLyrics
from ..text import Utilities 

def test_flow():
    substring = 'wait for it'
    SS = SpotifySearch()
    titles = SS.search(substring)

    YS = YouTubeSearch()
    #id = YS.search(title)

    AZ = AZLyrics()
    lyrics = AZ.download(titles[0]) 
    #print(lyrics)

    phonemes = {}



 

