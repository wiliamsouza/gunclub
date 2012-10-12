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
    if not request.user.is_staff:
        return HttpResponseForbidden()
    form = AddMemberForm()
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            profile = form.save(request)
            if request.POST.get('is_member'):
                profile.date_membership = datetime.date.today()
                profile.save()
                return HttpResponseRedirect(
                    reverse('edit_member', kwargs={'member_id': profile.id}))
            return HttpResponseRedirect(
                reverse('admin_dashboard',))
    return render_to_response(
        'member/edit.html',
        {'form': form,},
        context_instance=RequestContext(request)
        )


@login_required
def edit_member(request, member_id=0):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    member = None
    if member_id:
        member = get_object_or_404(Profile, id=member_id)
        form = EditMemberForm(instance=member)
    if request.method == 'POST':
        form = EditMemberForm(request.POST, instance=member)
        if form.is_valid():
            profile = form.save()
            if request.POST.get('is_member') and not member.date_membership:
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


@login_required
def upgrade_to_member(request, member_id=0):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    member = None
    if member_id:
        member = get_object_or_404(Profile, id=member_id)
        member.date_membership = datetime.date.today()
        member.is_member = True
        member.save()
        return HttpResponseRedirect(
            reverse('admin_dashboard',))
