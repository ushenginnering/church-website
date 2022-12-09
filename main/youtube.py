import requests
from django.conf import settings
from urllib.parse import urlparse

print(settings.GOOGLE_API_KEY)

def getVideoInfo(youtubeurl):
    res = requests.get(f"https://www.youtube.com/oembed?url={youtubeurl}&format=json&key={settings.GOOGLE_API_KEY}")
    path = urlparse(youtubeurl).path[1:]
    print(path)
    return res.json()['title'], path

