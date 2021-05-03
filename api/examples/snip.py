from argparse import ArgumentParser
from pprint import pprint

from ..search import SpotifySearch, YouTubeSearch
from ..download import AZLyrics, YoutubeDownload
from ..text import Utilities 

parser = ArgumentParser(description='Find a song with a few words')
parser.add_argument('_substring', type=str, help='Substring to be searched')

args = parser.parse_args()

substring = args._substring
SS = SpotifySearch()
results = SS.search(substring)
title = results[0]
total = results[1]

YS = YouTubeSearch()
id = YS.search(title)


AZ = AZLyrics()
lyrics = AZ.download(title) 

#TODO: create NLP wrapper class
utils = Utilities()
lyrics = utils.cleaned(lyrics, is_musical=True)
substring = utils.cleaned(substring)

phonemes = {}
#TODO: compose, pipe https://docs.python.org/3/library/itertools.html#itertools.chain
phonemes['lyrics'] = [p for term in lyrics.split() for p in utils.phonemes_of(term)]
phonemes['substring'] = [p for term in substring.split() for p in utils.phonemes_of(term)]
numSubstringPhonemes = len(phonemes['substring'])
numLyricsPhonemes = len(phonemes['lyrics'])
phonemes['lyrics'] = utils.concatenated(phonemes['lyrics'])
phonemes['substring'] = utils.concatenated(phonemes['substring'])

print(phonemes)
print(numSubstringPhonemes)
first = phonemes['lyrics'].index(phonemes['substring'])
start = ((first * total) / len(phonemes['lyrics'])) / 1000;
#TODO: rewrite this. currently counts whitespace
duration = ((numSubstringPhonemes * total) / len(phonemes['lyrics'])) / 1000;
print(start, duration)

YD = YoutubeDownload()
YD.download(id, title, start, duration)   


