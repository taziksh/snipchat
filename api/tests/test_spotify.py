import pytest
from ..search import SpotifySearch

def test_spotify_search():
    SS = SpotifySearch()
    #list of tuples!
    results = SS.search('close the door on your way out')
    print(results[0], results[1])
    
    