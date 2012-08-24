from django.test import TestCase


class LoginTest(TestCase):
    fixtures = ['users_data.json']

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()

    def test_redirect_to_login_home(self):
        response  = self.client.get('/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_redirect_to_login_dasboard_admin(self):
        response = self.client.get('/dashboard/admin/', follow=True)
        self.assertRedirects(
            response, '/accounts/login/?next=/dashboard/admin/'
            )

    def test_redirect_to_login_dashboard_user(self):
        response = self.client.get('/dashboard/user/', follow=True)
        self.assertRedirects(
            response, '/accounts/login/?next=/dashboard/user/'
            )
