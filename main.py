from flask import Flask
from flask_restx import Resource, Api, reqparse
import json
import os

app = Flask(__name__)

api = Api()
api.init_app(app)

parser = reqparse.RequestParser()
#hint: add artist album track name for higher match probability

@api.route('/test1')
class Main(Resource):
    parser.add_argument('query', type=str, help="Enter phrase from a lyrics -> get it as .mp3 snippet")
    def post(self):
        args = parser.parse_args()
        print(args)
        return args['query']


@api.route('/deezer')
class Deezer(Resource):
    parser.add_argument('query', type=str, help="Enter phrase from a lyrics -> get it as .mp3 snippet")
    def post(self):
        #TODO: deezer.py -> class 
        from api.deezer import intercept 
        args = parser.parse_args()
        query = args['query']
        print(query)
        lyrics = json.loads(intercept(query))
        return lyrics

@api.route('/youtube/download')
class YouTubeDownload(Resource):
    #TODO: parser.add_argument('
    def post(self):
        args = parser.parse_args()
        #TODO: importYD, YS...

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
        
