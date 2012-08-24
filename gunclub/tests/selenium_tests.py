from django.test import LiveServerTestCase

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver


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

    def test_login_admin(self):
        """ Test admin login

        Check if login form is working and the admin is redirected
        to the correct dashboard.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//button[@value="login"]').click()
        WebDriverWait(self.selenium, 10).until(
            lambda driver: \
            driver.find_element_by_xpath('//a[@href="/dashboard/admin/"]')
        )

    def test_login_user(self):
        """ Test user login

        Check if login form is working and the user is redirected
        to the correct dashboard.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('user')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//button[@value="login"]').click()
        WebDriverWait(self.selenium, 10).until(
            lambda driver: \
            driver.find_element_by_xpath('//a[@href="/dashboard/user/"]')
        )
