import pytest

from ..search import SpotifySearch

def test_spotify_search():
    SS = SpotifySearch()
    title = SS.search('wait for it')
    
    