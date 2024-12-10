import unittest
from unittest.mock import patch
from summarize import Summarize

class TestSummarize(unittest.TestCase):

    def test_summarize(self):
        summarize = Summarize()
        text = "This is a very long text that should be summarized."
        prompt = "Summarize this"
        
        summary = summarize.summarize(text, prompt)
        
        # Check that the summary is a string and not empty
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

    def test_process_data(self):
        summarize = Summarize()
        
        # Mock Reddit post and comments data
        response = [{
            "data": {
                "children": [{
                    "data": {
                        "selftext": "Post content to be summarized."
                    }
                }]
            }
        }, {
            "data": {
                "children": [{
                    "data": {
                        "body": "This is a comment."
                    }
                }]
            }
        }]
        
        # Call the method with the mock data
        result = summarize.process_data(response, "Summarize and highlight popular brands")
        
        # Verify that the result contains summaries
        self.assertIn("post_summary", result)
        self.assertIn("comments_summary", result)

if __name__ == '__main__':
    unittest.main()
