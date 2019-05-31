import requests
import time
import json
from bs4 import BeautifulSoup
from lxml import etree
#登录网址(五位.pdf)
url = "https://xpro-adl.91ctf.com/static/upload/teach/13/5b6c2946"

index_url = "https://xpro-adl.91ctf.com/teach/courseLearn?type=teach&id="

login_headers = {
    'cookie': 'route=da5109b4a956662d3c0e37f51ffef1de; php-console-server=5; token=eyJpdiI6Ims1K2xcLzcyVGRHY2x6ejZnYVk4a0lBPT0iLCJ2YWx1ZSI6Ik43RUFRK3JTa0ZIV2dmQTArb0hOdVQ0MDBJM0lXNHgrcWtlR2k2MGtLMmV5UzFyaG1ZZCt6N3QxaW5zOWZ6ZlhBa3F3dXpkbmZvM1V5Z05RVVpcL3o2TVlVQ3JVck01NExodGFcLzlWOXdOS3B2dWxNa0FYYjZJeWREa01mTjA0QXEiLCJtYWMiOiI3MzliMmM2MzM4MThhMDFkNTI3YmYwZTY1MzUxMGI2ZDk5MjU0ZTA4OTg2MTgwY2E0ZGVkYjFlYmY1NzdkNzA2In0%3D; adl=eyJpdiI6InhDSGZBZm00TTdQZUR1TFJ2QmVDcUE9PSIsInZhbHVlIjoib0s1WFhBTytNRDVHb1g5c1dUOHRLZzRsOXdrUGpWdThXekdsVUlaMTQxVjhDSmVzR0VSQWpZVDE2R3FOSGZPbGJpRXlzSmY5SGxPWG1TUXZqR0d0T0E9PSIsIm1hYyI6IjViMzIyZmEyZDI0MzAyYzMxNjgwNTMyZTEzMGI1ZjM2OTFlM2U0ZjRiY2UwMzE3MmNjMmYyMzBhNTdlZjI5ZDUifQ%3D%3D',
    'Host': 'xpro-adl.91ctf.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}

def edit_url(url, num):
    return url + num

def login(url,login_headers):
    r = requests.get(url, headers = login_headers)
    # print (r.json)
    return r.text

def resolver(code):
    soup=BeautifulSoup(code, features='lxml')
    span = soup.find_all('span', class_= 'clb-lessonname')
    for i in span:
        # print (i.contents)
        title = i.contents

    for tag in soup.find_all('a'):
        if tag.get('data-pdf') != None:
            # print(tag.get('data-pdf'))
            download_url = tag.get('data-pdf')
    return (str(title) + ':' 'https://xpro-adl.91ctf.com' + str(download_url))

for item in range(259):
    url_id = edit_url(index_url, str(item+1))
    codes = login(url_id,login_headers)
    download=resolver(codes)
    print (download)
    time.sleep(2)

# url_id = edit_url(index_url, str(2))
# codes = login(url_id,login_headers)
# resolver(codes)