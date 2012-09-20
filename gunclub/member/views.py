"""
Members views for gunclub
"""

import datetime

from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

from member.forms import AddMemberForm, EditMemberForm
from member.models import Profile


@login_required
def add_member(request):
    form = AddMemberForm()
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            profile = form.save(request)
            if request.POST.get('is_member'):
                profile.date_membership = datetime.date.today()
                profile.save()
                return HttpResponseRedirect(
                    reverse('edit_member',args=[profile.id]))
            return HttpResponseRedirect(
                reverse('admin_dashboard',))
    return render_to_response(
        'member/edit.html',
        {'form': form,},
        context_instance=RequestContext(request)
        )


def edit_member(request, member_id=0):
    member = None
    if member_id:
        member = get_object_or_404(Profile, id=member_id)
        form = EditMemberForm(instance=member)
    if request.method == 'POST':
        form = EditMemberForm(request.POST, instance=member)
        if form.is_valid():
            profile = form.save()
            if request.POST.get('is_member') and not profile.is_member:
                profile.date_membership = datetime.date.today()
                profile.save()
            return HttpResponseRedirect(
                reverse('admin_dashboard',))
    return render_to_response(
    'member/edit.html',
    {'form': form,
     'member_id': member_id},
    context_instance=RequestContext(request)
    )
