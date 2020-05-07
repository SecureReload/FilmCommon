## FilmCommon
Takes a movie script from IMSDb.com and outputs the most common words
## Social Media
[Twitter](https://twitter.com/SecureReload)
## Usage
Note - The formatting of film scripts on ISMDb.com can vary, because of this, some film scripts will return either no words at all, or very few.
```elm
FilmCommon.py [-h] [-u <url>] [-b] [-p]

Get 10 most common words from a film script from "imsdb.com"!

optional arguments:
  -h, --help  show this help message and exit
  -u <url>    URL of Script from "imsdb.com"
  -b          Remove the names of characters above their spoken lines.
  -p          Remove "pointless" words from being counted. For example: "the", "a", "this"...
```
