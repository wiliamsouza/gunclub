from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Password"))
    pass2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Password (again)"))

    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=30)),
                                 label=_('first name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=30)),
                                label=_('last name'))

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

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'pass1' in self.cleaned_data and 'pass2' in self.cleaned_data:
            if self.cleaned_data['pass1'] != self.cleaned_data['pass2']:
                error_msg = _("The two password fields didn't match.")
                raise forms.ValidationError(error_msg)
        return self.cleaned_data

    class Meta:
        exclude = ['user',]
        fiels = [
            'username',
            'email',
            'pass1',
            'pass2',
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
