"""
Profile and address models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.br.br_states import STATE_CHOICES


GENDER_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
)

RELATIONSHIP_CHOICES = (
    (1, _('Single')),
    (2, _('Married')),
    (3, _('Widower')),
    (4, _('Separeted')),
    (5, _('Legally Separeted')),
    (6, _('Divorced')),
)


class Profile(models.Model):
    """ Member profile

    Automatic create every time a new user is created.
    """
    user = models.OneToOneField(User)
    is_member = models.BooleanField(_('Is member'), default=False)
    date_membership = models.DateField(blank=True, null=True)
    job_position = models.CharField(_('Job position'), max_length=32,
                                    blank=True, null=True)
    gender = models.CharField(_('Gender'), max_length=1,
                              choices=GENDER_CHOICES, blank=True, null=True)
    relationship = models.IntegerField(_('Relationship'),
                                       choices=RELATIONSHIP_CHOICES,
                                       blank=True, null=True)
    spouse_name = models.CharField(_("Spouse name"), max_length=64,
                                 blank=True, null=True)
    father_name = models.CharField(_("Father's name"), max_length=64,
                                   blank=True, null=True)
    mother_name = models.CharField(_("Mother's name"), max_length=64,
                                   blank=True, null=True)

    date_of_birth = models.DateField(_('Date of birth'), blank=True, null=True)
    place_of_birth = models.CharField(_('Place of birth'), max_length=32,
                                      blank=True, null=True)

    # Brazilian related fields
    cpf = models.CharField(_('CPF'), max_length=14, blank=True, null=True)
    rg = models.CharField(_('RG'), max_length=14, blank=True, null=True)
    rg_issuing_institution = models.CharField(_('Issuing institution'),
                                              max_length=10, blank=True,
                                              null=True)
    rg_date_of_issue = models.DateField(_('Date of issue'), blank=True,
                                        null=True)

    has_cr = models.BooleanField(_('Has CR'), default=False, blank=True)
    cr_valid_thru = models.DateField(_('CR valid thru'), null=True, blank=True)

    invoice_due_day = models.IntegerField(blank=True, null=True)

    street = models.CharField(_('Street'), max_length=128,
                              blank=True, null=True)
    street2 = models.CharField(_('Street'), max_length=128,
                               blank=True, null=True)
    city = models.CharField(_('City'), max_length=32, blank=True, null=True)
    postal_code = models.CharField(_('Postal / Zip code'), max_length=9,
                                  blank=True, null=True)
    state_province = models.CharField(_('State / Province'), max_length=2,
                                      choices=STATE_CHOICES, blank=True,
                                      null=True)
    def __unicode__(self):
        return unicode(self.user.get_full_name()) #pylint: disable=E1101


#pylint: disable=W0613
def create_user_profile(sender, instance, created, **kwargs):
    """ Create user profile

    Handler for the User post_save signal that create a profile
    if one does not exist.
    """
    if created:
        Profile.objects.create(user=instance) #pylint: disable=E1101

post_save.connect(create_user_profile, sender=User)
