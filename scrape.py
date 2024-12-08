#!/usr/bin/env python
import requests
import json
import os
from dotenv import load_dotenv

# load sensitive info from .env
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')

# initialize authentication with reddit api
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
data = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD
}
headers = {'User-Agent': USER_AGENT}

# fetch the access token
res = requests.post(
    'https://www.reddit.com/api/v1/access_token',
    auth=auth, data=data, headers=headers
)
TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

# reddit post link
post_link = 'https://www.reddit.com/r/PHbuildapc/comments/18j55t3/recommendations_for_a_keyboard/'
post_link_split = post_link.split('/') # split the text between / 
subreddit = post_link_split[4] 
post_id = post_link_split[6]
url = f"https://oauth.reddit.com/r/{subreddit}/comments/{post_id}" # fetch
response = requests.get(url, headers=headers)
formatted_response = json.dumps(response.json(), indent=4) # format the json file before printing in terminal
print(formatted_response)

# save in response.json file
with open('response.json', 'w') as json_file:
    json.dump(response.json(), json_file, indent=4)
print('\nsaved in response.json')