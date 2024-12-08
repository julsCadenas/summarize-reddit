#!/usr/bin/env python
import requests
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

subreddit = "PHBuildapc"
post_id = "16u7dg8"
url = f"https://oauth.reddit.com/r/{subreddit}/comments/{post_id}"
response = requests.get(url, headers=headers)

print(response.json())
