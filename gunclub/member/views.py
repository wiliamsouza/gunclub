"""
Members views for gunclub 
"""

from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

from member.forms import MemberForm
from member.models import Profile


@login_required
def add_member(request):
    form = MemberForm()
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(request.user)
            return HttpResponseRedirect(
                reverse('admin_dashboard',))
    return render_to_response(
        'member/profile.html',
        {'form': form,},
        context_instance=RequestContext(request)
        )

