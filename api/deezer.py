import requests
import json
import pylcs

def DeezerSearch(query):
    session = requests.Session()
    response1 = session.get('https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&api_version=1.0&api_token=')
    #view cookies with: session.cookies.get_dict()

    api_token = response1.json()['results']['checkForm']
    response2 = session.post('https://www.deezer.com/ajax/gw-light.php?method=song.getLyrics&api_version=1.0&api_token='+api_token, data={'sng_id': 107832292})
    lyrics_sync_json = (json.loads(response2.text))['results']['LYRICS_SYNC_JSON']

    lyrics = []
    for i in range(len(lyrics_sync_json)):
        lyrics.append(lyrics_sync_json[i]['line'])
    #TODO: this should be its own function.

    lcs_lengths = pylcs.lcs_of_list(query, lyrics)
    print(lcs_lengths)
    max_index = lcs_lengths.index(max(lcs_lengths)) 
    return lyrics_sync_json[max_index]
