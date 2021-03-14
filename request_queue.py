import argparse
import re
import os
from property import redis_server

# This function is checking the format of youtube Url
def validation_youtube_url(url):
    if re.findall('^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$', url):   # validation for URL
        r = redis_server
        value = url
        r.lpush('url_key',value)  
        
    else:
        print('Please enter the correct Youtube Url')

parser = argparse.ArgumentParser(description="YouTube Video Data Extractor")
parser.add_argument("url", help="URL of the YouTube video")
args = parser.parse_args()
url = args.url

validation_youtube_url(url)  #calling validation_youtube_url function

