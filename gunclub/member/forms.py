"""
Member forms for gunclub 
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.sites.models import get_current_site
from django.utils.translation import ugettext_lazy as _
from registration.models import RegistrationProfile

from member.models import Profile

attrs_dict = {'class': 'required'}


class MemberForm(forms.ModelForm):
    """
    Most of this code came from django-registration form thanks James Bennett
    and is licensed under: https://bitbucket.org/ubernostrum/django-registration/src/27bccd108cde/LICENSE.
    """
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _("This value may "
                  "contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("E-mail"))
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=30)),
                                 label=_('first name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=30)),
                                label=_('last name'))

    def save(self, request):
        profile = Profile()
        user = RegistrationProfile.objects.create_inactive_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='$up3rS3cr3t',
            site=get_current_site(request),
            send_email=True,
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = User.objects.filter(
            username__iexact=self.cleaned_data['username'])
        if existing.exists():
            error_msg = _("A user with that username already exists.")
            raise forms.ValidationError(error_msg)
        else:
            return self.cleaned_data['username']

    class Meta:
        exclude = ['user',]
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_member',
            'job_position',
            'gender',
            'relationship',
            'wife_name',
            'father_name',
            'mother_name',
            'date_of_birth',
            'place_of_birth',
            'cpf',
            'rg',
            'rg_issuing_institution',
            'rg_date_of_issue',
            'has_cr',
            'cr_valid_thru',
            'invoice_due_day',
        ]
        model = Profile
