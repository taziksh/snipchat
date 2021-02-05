from flask import Flask
from flask_restx import Resource, Api, reqparse

from lyrics.spotify import search

app = Flask(__name__)

api = Api()
api.init_app(app)

parser = reqparse.RequestParser()
parser.add_argument('phrase', type=str, help="Enter phrase from a lyrics -> get it as .mp3 snippet")

@api.route('/snippet')
class SnippetBuilder(Resource):
    def post(self):
        """POST request with phrase payload (test this)"""
        args = parser.parse_args()
        tracks = search(args)
        return args

if __name__ == '__main__':
    app.run(debug=True)
        
