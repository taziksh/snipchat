from flask import Flask
from flask_restx import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import json
import os

from api.search import SpotifySearch
from api.download import YouTubeDownload
from api.text import Utilities 
#TODO: inb4 namespace collisions
from api.google import Cloud
from api.deezer import DeezerAPIFactory

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api()
api.init_app(app)

parser = reqparse.RequestParser()
parser.add_argument('query', case_sensitive=False, help="")
parser.add_argument('title', case_sensitive=False, help="")
parser.add_argument('duration', type=int,  help="")
parser.add_argument('start', help="")
#hint: add artist album track name for higher match probability

@api.route('/test1')
class Main(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        return args

@cross_origin()
@api.route('/search/spotify')
class Search(Resource):
    def post(self):
        """
        :returns: Spotify API results
        """
        args = parser.parse_args()
        query = args['query']
        SS = SpotifySearch()
        return SS.search(query)



parser_deezer = parser.copy()
@cross_origin()
@api.route('/deezer')
class DeezerRoute(Resource):
    def post(self):
        #TODO: s 
        args = parser_deezer.parse_args()
        title = args['title']
        query = args['query']
        duration = args['duration']

        utils = Utilities()
        YD = YouTubeDownload()

        DeezerAPI = DeezerAPIFactory()
        lyrics_sync_json = DeezerAPI.getLyrics(title) 
        resp = utils.lcs_index(query, lyrics_sync_json)
        #TODO:float -> int roundoff..
        #N.B. ffmpeg expects INT
        file_name = YD.download(title, duration,  int(resp['milliseconds'])/1000, int(resp['duration'])/1000+1)   
        cloud = Cloud()
        #TODO: create unique blob per invokation
        cloud.upload_blob("snipchat", file_name, "test1.mp3")
        public_url = cloud.make_blob_public("snipchat", "test1.mp3")
        return public_url


parser_youtubedownload = parser.copy()
@cross_origin()
@api.route('/youtube/download')
class YouTubeDownloadRoute(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        YD = YouTubeDownload()
        YD.download(args['title'], args['start'], args['duration'])   

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
        
