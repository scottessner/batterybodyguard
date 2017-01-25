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

        # He decides that he would like to create an account He clicks the signup link
        self.browser.find_element_by_id('a_signup').click()

        # He enters a username and password into the form
        user_field = self.browser.find_element_by_id('id_username')
        user_field.send_keys('iamauser')

        pw1_field = self.browser.find_element_by_id('id_password1')
        pw1_field.send_keys('P@ssw0rd')
        pw2_field = self.browser.find_element_by_id('id_password2')
        pw2_field.send_keys('P@ssw0rd')

        # He clicks submit to confirm creation
        self.browser.find_element_by_id('b_signup').click()

        # He verifies that the home page shows that he is logged in
        user_text = self.browser.find_element_by_id('logged_in_user')
        self.assertIn('iamauser', user_text.text)
