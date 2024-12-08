#!/usr/bin/env python
import json
from transformers import BartForConditionalGeneration, BartTokenizer

# initialize the model
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

# example text to be summarized (uncomment if u want to test)
# text = """
# Mechanical keyboards are highly popular in the Philippines for their tactile feel and customizability. 
# Many enthusiasts recommend brands like Keychron, Akko, and Royal Kludge for budget options, while 
# high-end enthusiasts go for GMK keycaps and switches like Cherry MX or Gateron. Finding the best mechanical keyboard 
# depends on your budget and preferences for size and typing feel.
# """

# open response.json (read only)
with open('response.json', 'r') as response:
    response = json.load(response)

# extract the post content
post_content = response[0]['data']['children'][0]['data'].get('selftext', '')

# extract the comments
comments = []
for comment in response[1]['data']['children']:
    if 'body' in comment['data']: 
        comments.append(comment['data']['body'])

# combine contents and comments
combined_text = post_content + '\n'.join(comments)
input_text = f"Summarize the top brands: \n{combined_text}"

# set the input parameters and prompt for the model
inputs = tokenizer.encode(
    input_text, 
    return_tensors="pt", 
    max_length=1024, 
    truncation=True
    )

# set teh parameters to be generated
summary_ids = model.generate(
    inputs, 
    max_length=130, 
    min_length=30, 
    length_penalty=2.0, 
    num_beams=4, 
    no_repeat_ngram_size=3,
    early_stopping=True
    )

# decodes the output of the summary_ids to be human readable 
summary = tokenizer.decode(
    summary_ids[0], 
    skip_special_tokens=True
    )

print("Summary:", summary)
