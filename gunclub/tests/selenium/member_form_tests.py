from django.test import LiveServerTestCase

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver


class MemberFormTest(LiveServerTestCase):
    fixtures = ['users_data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium  = WebDriver()
        super(MemberFormTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.selenium.quit()

    def test_required_field(self):
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

    def test_add_member_basic(self):
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('john')
        email_input = self.selenium.find_element_by_name('email')
        email_input.send_keys('john@johndoe.org')
        first_name_input = self.selenium.find_element_by_name('first_name')
        first_name_input.send_keys('John')
        last_name_input = self.selenium.find_element_by_name('last_name')
        last_name_input.send_keys('Doe')

    def test_add_member_full(self):
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('jane')
        email_input = self.selenium.find_element_by_name('email')
        email_input.send_keys('jane@janedoe.org')
        first_name_input = self.selenium.find_element_by_name('first_name')
        first_name_input.send_keys('Jane')
        last_name_input = self.selenium.find_element_by_name('last_name')
        last_name_input.send_keys('Doe')
        is_member_input = self.selenium.find_element_by_name('is_member')
        is_member_input.click()
        job_position_input = self.selenium.find_element_by_name('job_position')
        job_position_input.send_keys('Anonymous character')
        gender_input = Select(self.selenium.find_element_by_name('gender'))
        gender_input.select_by_visible_text('Female')
        relationship_input = Select(self.selenium.find_element_by_name('relationship'))
        relationship_input.select_by_visible_text('Married')
        wife_name_input = self.selenium.find_element_by_name('wife_name')
        wife_name_input.send_keys('John Doe')
        father_name_input = self.selenium.find_element_by_name('father_name')
        father_name_input.send_keys('John Roe')
        mother_name_input = self.selenium.find_element_by_name('mother_name')
        mother_name_input.send_keys('Jane Roe')
        date_of_birth_input = self.selenium.find_element_by_name('date_of_birth')
        date_of_birth_input.send_keys('06/06/1981')
        place_of_birth_input = self.selenium.find_element_by_name('place_of_birth')
        place_of_birth_input.send_keys('Antonina')
        cpf_input = self.selenium.find_element_by_name('cpf')
        cpf_input.send_keys('05505555555')
        rg_input = self.selenium.find_element_by_name('rg')
        rg_input.send_keys('55555555')
        rg_issuing_institution_input = self.selenium.find_element_by_name('rg_issuing_institution')
        rg_issuing_institution_input.send_keys('ssppr')
        rg_date_of_issue_input = self.selenium.find_element_by_name('rg_date_of_issue')
        rg_date_of_issue_input.send_keys('06/06/1995')
        has_cr_input = self.selenium.find_element_by_name('has_cr')
        has_cr_input.click()
        cr_valid_thru_input = self.selenium.find_element_by_name('cr_valid_thru')
        cr_valid_thur_input.send_keys('06/06/2013')
        invoice_due_day_input = self.selenium.find_element_by_name('invoice_due_day')
        invoice_due_day_input.send_keys('06')
