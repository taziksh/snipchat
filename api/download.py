import pysnooper
from abc import ABC, abstractmethod 
from azapi import AZlyrics
import youtube_dl, subprocess

from api.search import YouTubeSearch

class Download(ABC):

    @abstractmethod
    def download(self):
        pass

class AZLyrics(Download):
    def __init__(self):
        self.az = AZlyrics('google')

    #TODO: play with confidence level
    def download(self, title):
        self.az.title = title
        return self.az.getLyrics()
        
class YouTubeDownload(Download):
    #TODO: heuristic for finding video w/ same length
    def __init__(self):
        pass
    #TODO: will downgrade of video affect audio quality
    #TODO: append artist name to file - possibly UUID for online storage
    def download(self, title, spotifyDuration, _start, _duration):
        YS = YouTubeSearch()
        id = YS.search(title, spotifyDuration)
        self.url = "https://www.youtube.com/watch?v=" + id
        self.start = str(_start) 
        self.duration =  str(_duration)
        print(self.start, self.duration)
        #TODO: include timestamps in filename
        self.target = title + self.start + ":" + self.duration + ".mp3"
        with youtube_dl.YoutubeDL({'format': 'best', 'verbose': True}) as yt_dl:
            result = yt_dl.extract_info(self.url, download=False)
            video = result['entries'][0] if 'entries' in result else result
        '''
        ffmpeg params:
            -vn: no video
            -y: overwrite existing file
        '''
        subprocess.run(["ffmpeg", "-ss", self.start, "-i", video['url'], "-t", self.duration, "-vn", "-y", self.target])
        return self.target

