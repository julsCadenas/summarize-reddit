import unittest
from unittest.mock import patch
from scrape import Scrape

class TestScrape(unittest.TestCase):

    @patch('requests.post')
    def test_authenticate_success(self, mock_post):
        # Mock the response for authentication
        mock_post.return_value.json.return_value = {'access_token': 'mock_token'}
        
        scraper = Scrape()
        scraper.authenticate()  # This should call the mocked POST request
        
        # Check that the token is set correctly
        self.assertEqual(scraper.TOKEN, 'mock_token')
        self.assertTrue('Authorization' in scraper.headers)
        self.assertEqual(scraper.headers['Authorization'], 'bearer mock_token')

    @patch('requests.get')
    @patch('requests.post')
    def test_fetch_post(self, mock_post, mock_get):
        # Mock the response for authentication
        mock_post.return_value.json.return_value = {'access_token': 'mock_token'}
        
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
        scraper.authenticate()  # This should authenticate using the mock POST response
        
        # Now, fetch the post
        response = scraper.fetch_post('https://www.reddit.com/r/test/comments/123456/test_post/')
        
        # Verify that the response contains the correct post data
        self.assertIn('data', response)
        self.assertIn('children', response['data'])
        self.assertEqual(response['data']['children'][0]['data']['selftext'], 'This is a test post')

if __name__ == '__main__':
    unittest.main()
