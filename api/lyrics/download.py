from azapi import AZlyrics

api = AZlyrics('google')

# TODO: worth removing speaker names for musicals?
# EXAMPLE: [?;:,"'.]
def clean(lyrics):
    pass


def download(title):
# We are Searching for Meghan's lyrics "All about that bass"
    api.title = title
    lyrics = api.getLyrics()
    return clean(lyrics)
