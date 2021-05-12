import requests
import json

def DeezerSearch(title):
    session = requests.Session()
    response1 = session.get('https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&api_version=1.0&api_token=')
    #view cookies with: session.cookies.get_dict()

    api_token = response1.json()['results']['checkForm']
    response2 = session.post('https://www.deezer.com/ajax/gw-light.php?method=song.getLyrics&api_version=1.0&api_token='+api_token, data={'sng_id': 107832292})
    lyrics_sync_json = (json.loads(response2.text))['results']['LYRICS_SYNC_JSON']
    return lyrics_sync_json


    #TODO: this should be its own function.
