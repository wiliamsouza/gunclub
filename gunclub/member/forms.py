"""
Member forms for gunclub 
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.sites.models import get_current_site
from django.utils.translation import ugettext_lazy as _
from registration.models import RegistrationProfile

from member.models import Profile


class AddMemberForm(forms.ModelForm):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may "
                  "contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(max_length=75, label=_("E-mail"))
    first_name = forms.CharField(max_length=30, label=_('first name'))
    last_name = forms.CharField(max_length=30, label=_('last name'))

    def save(self, request, *args, **kwargs):
        user = RegistrationProfile.objects.create_inactive_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='$up3rS3cr3t',
            site=get_current_site(request),
            send_email=True,
        )
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        profile = user.get_profile()
        profile.rg = self.cleaned_data.get('rg')
        profile.cpf = self.cleaned_data.get('cpf')
        profile.date_of_birth = self.cleaned_data.get('date_of_birth')
        profile.job_position = self.cleaned_data.get('job_position')
        profile.is_member = self.cleaned_data.get('is_member') 
        profile.save()
        return profile

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
            'rg',
            'cpf',
            'date_of_birth',
            'job_position',
            'is_member',
        ]
        model = Profile


class EditMemberForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label=_('first name'))
    last_name = forms.CharField(max_length=30, label=_('last name'))
    email = forms.EmailField(max_length=75, label=_("E-mail"))

    def __init__(self, *args, **kwargs):
        super(EditMemberForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

    def save(self, *args, **kwargs):
        super(EditMemberForm, self).save(*args, **kwargs)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.email = self.cleaned_data.get('email')
        self.instance.user.save()

    class Meta:
        exclude = ['user',]
        fields = [
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
