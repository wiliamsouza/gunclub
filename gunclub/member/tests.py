from django.test import LiveServerTestCase

from selenium.webdriver.firefox.webdriver import  WebDriver

class LoginTest(LiveServerTestCase):
    fixtures = ['admin_data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium  = WebDriver()
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDowClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.selenium.quit()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//button[@value="login"]').click()
