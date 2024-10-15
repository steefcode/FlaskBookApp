import unittest
from Main import app

class HealthCheckTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint(self):
        # Send a GET request to /health
        response = self.app.get('/health')
        
        # Assert the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert the response is JSON
        self.assertEqual(response.content_type, 'application/json')

        # Parse the JSON response and assert the 'status' field
        data = response.get_json()
        self.assertEqual(data['status'], 'UP')
    
    def test_add_book(self):
        # Test data for adding a book
        new_book = {'title': 'The Lord of the Rings'}

        # Send POST request to add a book
        response = self.app.post('/books', json=new_book)

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Assert that the response content type is JSON
        self.assertEqual(response.content_type, 'application/json')

        # Parse the response JSON
        data = response.get_json()

        # Assert the book was added with an 'id' and correct 'title'
        self.assertIn('id', data)
        self.assertEqual(data['title'], new_book['title'])    

if __name__ == '__main__':
    unittest.main()
