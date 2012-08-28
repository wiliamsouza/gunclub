""" Login required as redirect tests.
"""

from django.test import TestCase


class LoginTest(TestCase):
    fixtures = ['users_data.json']

    def test_login_required_home(self):
        response  = self.client.get('/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_login_required_admin_dasboard(self):
        response = self.client.get('/dashboard/admin/', follow=True)
        self.assertRedirects(
            response, '/accounts/login/?next=/dashboard/admin/'
            )

    def test_login_required_user_dashboard(self):
        response = self.client.get('/dashboard/user/', follow=True)
        self.assertRedirects(
            response, '/accounts/login/?next=/dashboard/user/'
            )

    def test_not_staff_forbidden_admin_dashboard(self):
        self.client.login(username='user', password='secret')
        response = self.client.get('/dashboard/admin/')
        self.assertEqual(response.status_code, 403)
