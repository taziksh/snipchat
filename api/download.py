from abc import ABC, abstractmethod 

from azapi import AZlyrics

import youtube_dl, subprocess
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
        
class YoutubeDownload(Download):
    #TODO: heuristic for finding video w/ same length
    #TODO: will downgrade of video affect audio quality
    def __init__(self):
        pass
    def download(self, id, title, _start, _duration):
        self.url = "https://www.youtube.com/watch?v=" + id
        self.start = str(_start) 
        self.duration =  str(_duration)
        self.target = title + ".mp4"
        with youtube_dl.YoutubeDL({'format': 'best'}) as yt_dl:
            result = yt_dl.extract_info(self.url, download=False)
            video = result['entries'][0] if 'entries' in result else result
        subprocess.run(["ffmpeg", "-ss", self.start, "-i", video['url'], "-t", self.duration, "-c", "copy", self.target])

