from requests_html import HTMLSession 
from property import redis_server,schedule_frequency        # importing redis_conf
from bs4 import BeautifulSoup as bs      # importing BeautifulSoup
import os
import schedule                          # importing schedule
import time                              # importing time


def extracting_url(url):
    # init session
    session = HTMLSession()
    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(sleep=1)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    return soup


# This function is used to extracting the data from the Youtube url
def get_video_details(url):
    soup = extracting_url(url)
    # initialize the result
    result = {}
    # video title
    result["title"] = soup.find("h1").text.strip()
    # video views (converted to integer)
    result["views"] = int(''.join([ c for c in soup.find("span", attrs={"class": "view-count"}).text if c.isdigit() ]))
    # video description
    result["description"] = soup.find("yt-formatted-string", {"class": "content"}).text
    # date published
    result["date_published"] = soup.find("div", {"id": "date"}).text[1:]
    # get the duration of the video
    result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    # get the video tags
    result["tags"] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])
    # channel details
    channel_tag = soup.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a")
    # channel name
    channel_name = channel_tag.text
    # channel URL
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subscribers as str
    channel_subscribers = soup.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    return result


def print_save_data(data):
    if data['title']:
            print(f"Title: {data['title']}")             # printing data
            r.lpush('title',data['title'])               # adding video information in Redis List
    else:
        print("Title: Empty")
        r.lpush('title','empty')

    if data['tags']:
        print(f"Video tags: {data['tags']}")
        r.lpush('Video tags',data['tags'])
    else:
        print("Video tags: Empty")
        r.lpush('Video tags','Empty')

    if data['views']:
        print(f"Views: {data['views']}")
        r.lpush('Views',data['views'])
    else:
        print("Views:0 ")
        r.lpush('Views',0)

    if data['date_published']:
        print(f"Upload Date: {data['date_published']}")
        r.lpush('Upload Date',data['date_published'])
    else:
        print("Upload Date:Empty")
        r.lpush('Upload Date',0)

    if data['channel']['name']:
        print(f"\nChannelTitle: {data['channel']['name']}")
        r.lpush('channel Title',data['channel']['name'])
    else:
        print("channelTitle:Empty")
        r.lpush('channel Title','empty')

    if data['channel']['subscribers']:
        print(f"Channel Subscribers: {data['channel']['subscribers']}")
        r.lpush('Channel Subscribers',data['channel']['subscribers'])
    else:
        print("Channel Subscribers:0")
        r.lpush('Channel Subscribers','empty')

    if data['duration']:
        print(f"Video Duration: {data['duration']}")
        r.lpush('Video Duration',data['duration'])
    else:
        print("Video Duration:0")
        r.lpush('Video Duration',0)
    if data['description']:
        print(f"\nDescription: {data['description']}\n")
        r.lpush('Description',data['description'])
    else:
        print("Description:empty")
        r.lpush('Description','empty')


# this function is used to  fetching the url from redis list and print the extracted you tube data
def fetching_url():
    url = r.lpop('url_key')                      #pop the url from redis list  
    if url:
        print("Extracting data Please Wait...........................") 
        data = get_video_details(url)       
        print_save_data(data)

        # Automatic execute the request_save.py 
        os.system('python3 request_save.py')
    else:
        pass

r = redis_server
r.lpush('pid',os.getpid())     # push process id in redis list for terminating procees when requried
print(os.getpid()) 

schedule.every(schedule_frequency).seconds.do(fetching_url)   # Running  request_process.py script independently
while 1:
    schedule.run_pending()
    time.sleep(1)


    