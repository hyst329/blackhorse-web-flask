import unittest
import urllib.request

from flask_testing import LiveServerTestCase
from selenium import webdriver
from flask_chess import app

class TestChess(LiveServerTestCase):

    def create_app(self):
        return app
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
