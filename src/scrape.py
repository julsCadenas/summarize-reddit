import requests
import json
import os
from dotenv import load_dotenv

class Scrape:
    def __init__(self):
        load_dotenv()
        self.CLIENT_ID = os.getenv('CLIENT_ID')
        self.CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        self.USERNAME = os.getenv('USERNAME')
        self.PASSWORD = os.getenv('PASSWORD')
        self.USER_AGENT = os.getenv('USER_AGENT')
        self.TOKEN = None
        self.headers = {'User-Agent': self.USER_AGENT}

    def authenticate(self):
        auth = requests.auth.HTTPBasicAuth(self.CLIENT_ID, self.CLIENT_SECRET)
        data = {
            'grant_type': 'password',
            'username': self.USERNAME,
            'password': self.PASSWORD
        }
        res = requests.post(
            'https://www.reddit.com/api/v1/access_token',
            auth=auth, data=data, headers=self.headers
        )
        res.raise_for_status()
        self.TOKEN = res.json()['access_token']
        self.headers['Authorization'] = f'bearer {self.TOKEN}'

    def save_into_json(self, response, filename):
        with open(filename, 'w') as json_file:
            json.dump(response.json(), json_file, indent=4)
        print('saved in response.json')

    def fetch_post(self, post_link):
        post_link_split = post_link.split('/')
        subreddit = post_link_split[4]
        post_id = post_link_split[6]
        url = f"https://oauth.reddit.com/r/{subreddit}/comments/{post_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        self.save_into_json(response, "../data/response.json")
        return response.json()