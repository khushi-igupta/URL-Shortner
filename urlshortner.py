#URL SHORTENER which is used to reduce long links
# TestCase = "https://www.google.com/search?q=codeclause&oq=codeclause&aqs=chrome..69i57.4522j0j7&sourceid=chrome&ie=UTF-8"

import pyshorteners

url = input('Enter url: ')

def shortenurl(url):
    s = pyshorteners.Shortener()
    print("Short url is: " + s.tinyurl.short(url))

shortenurl(url)