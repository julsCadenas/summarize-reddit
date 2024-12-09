# Reddit Post Summarizer

This project is a Python script that fetches a Reddit post and its comments, processes them using the Reddit API, and generates a summary using the BART transformer model.

## Status: 🚧 Under Development

This project is currently a work in progress. While the core functionality is operational, additional features, improvements, and bug fixes are actively being worked on. Feedback and contributions are welcome!

## Features
- Fetches Reddit posts and comments using the Reddit API.
- Summarizes large text content using the `facebook/bart-large-cnn` model from Hugging Face.
- Stores fetched Reddit data in a JSON file (`response.json`).

## Requirements
- Required Python packages (install via pip):
  - `transformers`
  - `requests`
  - `dotenv`
  - `torch`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/reddit-post-summarizer.git
   cd reddit-post-summarizer
   ```
2. Set up your environmental variables
3. Run main.py
