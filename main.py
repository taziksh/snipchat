from flask import Flask
from flask_restx import Resource, Api, reqparse
import json
import os

from api.download import YouTubeDownload
from api.deezer import DeezerSearch 

app = Flask(__name__)

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
@api.route('/deezer')
class DeezerRoute(Resource):
    def post(self):
        #TODO: s 
        args = parser_deezer.parse_args()
        query = args['query']
        return DeezerSearch() 

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
        
