import praw
import json
import os
from dotenv import load_dotenv

load_dotenv()
reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    user_agent = "retldr"
)

data = []
subreddit = reddit.subreddit("PHbuildapc")  

for submission in subreddit.top(limit=100): 
    post = {
        "title": submission.title,
        "selftext": submission.selftext,
        "comments": [
            comment.body for comment in submission.comments
            if isinstance(comment, praw.models.Comment)
        ]
    }
    data.append(post)

# Save to JSON
with open("reddit_data.json", "w") as file:
    json.dump(data, file, indent=4)
