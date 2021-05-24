import requests
import json
from requests_html import HTMLSession

class DeezerAPIFactory:
    def __init__(self):
        pass
    def getLyrics(self, title):
        session = requests.Session()
        response1 = session.get('https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&api_version=1.0&api_token=')
        #view cookies with: session.cookies.get_dict()
        trackId = self.getTrackId(title)
        print('trackId: ', trackId)

        api_token = response1.json()['results']['checkForm']
        response2 = session.post('https://www.deezer.com/ajax/gw-light.php?method=song.getLyrics&api_version=1.0&api_token='+api_token, data={'sng_id': trackId})
        lyrics_sync_json = (json.loads(response2.text))['results']['LYRICS_SYNC_JSON']
        return lyrics_sync_json

    def getTrackId(self, query):
        session = HTMLSession()
        r = session.get('https://google.com/search?q='+query+' site:deezer.com')
        #Top 5 Google Search results
        for i in range(1, 5):
            selector = f'div.g:nth-child({i}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)'
            a_html = r.html.find(selector, containing='track')
            print('html: ', a_html)
            if len(a_html) == 0:
                continue
            url = a_html[0].attrs['href']
            print('url: ', url)
            index = url.find('track')
            if index != -1:
                return url[index+6:]
                    


