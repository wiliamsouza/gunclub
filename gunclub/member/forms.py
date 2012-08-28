from django import forms

from member.models import Profile

class MemberForm(forms.ModelForm):
    class Meta:
        model = Profile
