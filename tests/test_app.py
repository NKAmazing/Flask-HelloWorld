# Description: Test cases of the application

# Python imports
import unittest
import json
from app import app

class AppTestCase(unittest.TestCase):
    '''
    Class that inherits from Unittest Library to test the application
    '''
    def setUp(self):
        '''
        Method to set up the test client
        '''
        self.app = app.test_client()

    def test_index(self):
        '''
        Method to test the index route
        '''
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Hello, World!'})

if __name__ == '__main__':
    '''
    Start the unit test
    '''
    unittest.main()