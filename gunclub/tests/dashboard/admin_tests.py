""" Admin dashboard tests.
"""
from django.test import TestCase


class AdminTest(TestCase):
    fixtures = ['users_data.json']

    def test_admin_dashboard(self):
        self.client.login(username='admin', password='secret')
        response = self.client.get('/dashboard/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['members']), 2)
        self.assertEqual(response.context['title'], 'Admin dashboard')

    def test_user_dashboard(self):
        self.client.login(username='user', password='secret')
        response = self.client.get('/dashboard/user/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['members']), 2)
        self.assertEqual(response.context['title'], 'User dashboard')
