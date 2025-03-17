#!/usr/bin/env python
from summarize import Summarize
from scrape import  Scrape
import json
import os

def save_summary(summary_data, file_path):
    if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)  
                if not isinstance(data, list):
                    data = [data]  
            except json.JSONDecodeError:
                data = []  
    else:
        data = [] 

    data.append(summary_data)
    print("Summary appended!")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("File updated!")

def main():
    scraper = Scrape()
    summarize = Summarize()

    scraper.authenticate()
    post_link = 'https://www.reddit.com/r/ITPhilippines/comments/1irc5ix/83k_monthly_as_senior_software_engineer_fair_ba/'
    response = scraper.fetch_post(post_link)
    summary = summarize.process_data(response, "Summarize and highlight popular brands")
    
    print("Post Summary:", json.dumps(summary["post_summary"], indent=4))
    print("Comments Summary:", json.dumps(summary["comments_summary"], indent=4))

# save_summary(summary, '../data/summary.json')
        
if __name__ == "__main__":
    main()
    
# test pushc