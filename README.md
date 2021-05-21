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

## Features TBD
- [] Search bar types i.e. general, playlists,artists, albums on Spotify. Example use case: "breakdown breakdown" to find JJBA IV op
- [] Allow users to 'snip' custom track lengths
- Authenticate with Spotify - BYOT ('token') to handle more users (OFC, not even relevant until we can scale the lyrics acquisition process haha)
- Bill clients for Google Cloud storage

## Snipchat Web

### Design Decisions
Learning is a haphazard process. It is not always feasible for me to note things down as I write them. Unless I make it very low-effort to do, that is.
- [Uncontrolled vs. controlled components](https://goshakkk.name/controlled-vs-uncontrolled-inputs-react/): you will encounter the latter in ReactJS, particularly if you use component libraries. Something to be aware of as you scour internet forums and documentation.
- Callbacks: this is (one) way to pass props 'up the DOM tree' from children to parents. Again, this is a commonly encountered pattern. E.g. I'm not writing my own HTML <input> components. Instead, I'm using callbacks and passing props to this controlled component (I am the controller btw). Also, there's this other thing called prop drilling which may be related.

### N.B.
- [You can't use browser-based tools for Spotify Web API](https://github.com/thelinmichael/spotify-web-api-node/issues/257). You have to use a server-side setup because clientside is vulnerable to secret exposure

### Resources
I find myself referring to these resources often.
- https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox
