""" Member application tests.
"""

from datetime import date

from django.test import TestCase
from django.contrib.auth.models import User

from member.models import Profile


# pylint: disable=R0904
class ProfileTest(TestCase):
    """ Main class for profile tests
    """

    def test_create_normal_user(self):
        """ Test creation of normal user.
        """
        user = User.objects.create_user('normaluser',
                                        'normaluser@gunclub.org',
                                        'secret')
        user.first_name = 'Normal'
        user.last_name = 'User'
        user.save()
        profile = user.get_profile()
        profile.rg = '55555555555555'
        profile.cpf = '66666666666666'
        profile.date_of_birth = date(1981, 06, 06)
        profile.job_position = 'shootershootershootershootershoo'
        profile.save()

        # pylint: disable=E1101
        profiles_in_db = Profile.objects.filter(is_member=False)
        self.assertEquals(len(profiles_in_db), 1)
        profile_in_db = profiles_in_db[0]
        self.assertEquals(profile_in_db, profile)
        self.assertEquals(str(profile_in_db), user.get_full_name())

    def test_create_member_user(self):
        """ Test creation of member user.
        """
        # pylint: disable=E1101
        user = User.objects.create_user('memberuser',
                                        'normaluser@gunclub.org',
                                        'secret')
        user.first_name = 'Member'
        user.last_name = 'User'
        user.save()
        profile = user.get_profile()
        profile.is_member = True
        profile.rg = '55555555555555'
        profile.cpf = '66666666666666'
        profile.date_of_birth = date(1981, 06, 06)
        profile.job_position = 'shootershootershootershootershoo'
        profile.gender = 'M'
        profile.relationship = 1
        profile.wife_name = 'Wife Name'
        profile.father_name = 'Father Name'
        profile.mother_name = 'Mother Name'
        profile.place_of_birth = 'Brazil Parana Antonina'
        profile.rg_issuing_institution = 'SSPPR'
        profile.rg_date_of_issue = date.today()
        profile.has_cr = True
        profile.cr_valid_thru = date(2014, 06, 05)
        profile.invoice_due_day = 10
        profile.save()

        # pylint: disable=E1101
        profiles_in_db = Profile.objects.filter(is_member=True)
        self.assertEquals(len(profiles_in_db), 1)
        profile_in_db = profiles_in_db[0]
        self.assertEquals(profile_in_db, profile)
        self.assertEquals(str(profile_in_db), user.get_full_name())
