#!/usr/bin/env python
from summarize import Summarize
from scrape import  Scrape
import json

def main():
    scraper = Scrape()
    summarize = Summarize()

    scraper.authenticate()
    post_link = 'https://www.reddit.com/r/phcareers/comments/z1ml65/best_budgetfriendly_ergonomic_chair_for_wfh/'
    response = scraper.fetch_post(post_link)
    summary = summarize.process_data(response, "Summarize and highlight popular brands")
    
    print("Post Summary:", json.dumps(summary["post_summary"], indent=4))
    # print("Comments Summary:", json.dumps(summary["comments_summary"], indent=4))

if __name__ == "__main__":
    main()
    
# test pushc