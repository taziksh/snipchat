from flask import Flask
from flask_restx import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import json
import os

from api.download import YouTubeDownload
from api.text import Utilities 
#inb4 namespace collisions
from api.google import Cloud
from api.deezer import DeezerAPIFactory

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api()
api.init_app(app)

parser = reqparse.RequestParser()
parser.add_argument('query', case_sensitive=False, help="")
parser.add_argument('title', case_sensitive=False, help="Song title on YouTube")
parser.add_argument('start', help="")
parser.add_argument('duration',  help="")
#hint: add artist album track name for higher match probability

@api.route('/test1')
class Main(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        return args


parser_deezer = parser.copy()
@cross_origin()
@api.route('/deezer')
class DeezerRoute(Resource):
    def post(self):
        #TODO: s 
        args = parser_deezer.parse_args()
        title = args['title']

        utils = Utilities()
        YD = YouTubeDownload()

        DeezerAPI = DeezerAPIFactory()
        lyrics_sync_json = DeezerAPI.getLyrics(title) 
        resp = utils.lcs_index(title, lyrics_sync_json)
        #TODO:float -> int roundoff..
        #N.B. ffmpeg expects INT
        file_name = YD.download(title, int(resp['milliseconds'])/1000, int(resp['duration'])/1000+1)   
        cloud = Cloud()
        #TODO: create unique blob per invokation
        cloud.upload_blob("snipchat", file_name, "test1.mp3")
        public_url = cloud.make_blob_public("snipchat", "test1.mp3")
        return public_url


parser_youtubedownload = parser.copy()
@api.route('/youtube/download')
class YouTubeDownloadRoute(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        YD = YouTubeDownload()
        YD.download(args['title'], args['start'], args['duration'])   

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
        
