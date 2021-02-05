import pytest

from pprint import pprint

from ..search import SpotifySearch, YoutubeSearch

def test_flow():
    ss = SpotifySearch()
    title = ss.search('wait for it')

    ys = YoutubeSearch()
    print(ys.search(title))
    '''
    from ..lyrics.spotify import search as search_lyrics
    from ..lyrics.download import download as get_lyrics
    from ..youtube.search import search as search_videos

    title = search_lyrics("wait for it")
    pprint(title)
    
    lyrics = get_lyrics(title)
    print(lyrics)
    
    video_id = search_videos(title)
    pprint(video_id)
    '''
    pass
 

