from transformers import BartForConditionalGeneration, BartTokenizer

tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

text = """
Mechanical keyboards are highly popular in the Philippines for their tactile feel and customizability. 
Many enthusiasts recommend brands like Keychron, Akko, and Royal Kludge for budget options, while 
high-end enthusiasts go for GMK keycaps and switches like Cherry MX or Gateron. Finding the best mechanical keyboard 
depends on your budget and preferences for size and typing feel.
"""

inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=130, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Summary:", summary)
