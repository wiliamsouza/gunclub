from django.test import LiveServerTestCase
from django.test import Client

from selenium.webdriver.firefox.webdriver import  WebDriver

class LoginTest(LiveServerTestCase):
    fixtures = ['users_data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium  = WebDriver()
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.selenium.quit()

    def test_redirect_to_login(self):
        client = Client()
        response  = client.get('/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/')

"""
    def test_login_admin(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//button[@value="login"]').click()

    def test_login_user(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('user')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//button[@value="login"]').click()
"""
