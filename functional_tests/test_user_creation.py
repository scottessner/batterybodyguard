from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(FunctionalTest):

    def test_can_create_a_user(self):
        # Scott checks out the batterybodyguard site
        self.browser.get(self.server_url)

        # He sees the page title and verifies it's a battery site
        self.assertIn('Battery Bodyguard', self.browser.title)

        time.sleep(10)

