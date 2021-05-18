# Snipchat

## Introduction
Snipchat returns audio snippets based on a given input phrase.

## Building
- Run a full example by `python example.py <arg1>...` from the /api directory
- API request and docs will be available soon (use Postman's Doc generator!)

## Style Guide
- Use single quotes by default, and double quotes for string literals
- For functions that mutate arguments, use verb conjugation (See https://stackoverflow.com/a/8211949/8773953) 
- Classes follow PascalCase, but note that we maintain proper nouns e.g. 'YouTube', versus 'Youtube', 'AZLyrics' vs 'Azlyrics'
- Classes are used for abstraction. The Abstract Factory design pattern is employed for the generic Download and Search functionality. This is then concretized with specific API-based classes e.g. 'YouTubeDownload' and 'YouTubeSearch'

## Future Features
- [] Search bars e.g. playlists,artists, albums on Spotify. Example use case: "breakdown breakdown" to find JJBA IV op
- Authenticate with Spotify - BYOT ('token') to handle more users (OFC, not even relevant until we can scale the lyrics acquisition process haha)
- Bill clients for Google Cloud storage
