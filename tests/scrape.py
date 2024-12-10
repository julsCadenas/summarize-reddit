import unittest
from unittest.mock import patch
from scrape import Scrape

class TestScrape(unittest.TestCase):

    @patch('requests.post')
    def test_authenticate_success(self, mock_post):
        # Mock successful response with access token
        mock_post.return_value.json.return_value = {'access_token': 'mock_token'}
        scraper = Scrape()
        scraper.authenticate()
        
        # Check that the token is set correctly
        self.assertEqual(scraper.TOKEN, 'mock_token')
        self.assertTrue('Authorization' in scraper.headers)
        self.assertEqual(scraper.headers['Authorization'], 'bearer mock_token')

    @patch('requests.get')
    def test_fetch_post(self, mock_get):
        # Mock a sample response for fetching a post
        mock_get.return_value.json.return_value = {
            "data": {
                "children": [{
                    "data": {
                        "selftext": "This is a test post"
                    }
                }]
            }
        }
        scraper = Scrape()
        scraper.authenticate()
        response = scraper.fetch_post('https://www.reddit.com/r/test/comments/123456/test_post/')
        
        # Verify that the response contains the correct post data
        self.assertIn('data', response)
        self.assertIn('children', response['data'])

if __name__ == '__main__':
    unittest.main()
