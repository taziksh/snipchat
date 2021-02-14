from abc import ABC, abstractmethod 

from azapi import AZlyrics

class Download(ABC):

    @abstractmethod
    def download(self):
        pass

class AZLyrics(Download):
    def __init__(self):
        self.az = AZlyrics('google')

    #TODO: confidence level
    def download(self, title):
        self.az.title = title
        return self.az.getLyrics()
        