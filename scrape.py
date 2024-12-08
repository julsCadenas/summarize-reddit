#!/usr/bin/env python
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
data = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD
}
headers = {'User-Agent': USER_AGENT}

res = requests.post(
    'https://www.reddit.com/api/v1/access_token',
    auth=auth, data=data, headers=headers
)
TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

post_link = 'https://www.reddit.com/r/PHbuildapc/comments/16u7dg8/mechanical_keyboard_recommendation/'
post_link_split = post_link.split('/')
subreddit = post_link_split[4]
post_id = post_link_split[6]
url = f"https://oauth.reddit.com/r/{subreddit}/comments/{post_id}"
response = requests.get(url, headers=headers)
formatted_response = json.dumps(response.json(), indent=4)
print(formatted_response)
