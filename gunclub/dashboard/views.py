"""
Root view for gunclub project
"""

from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

from member.forms import AddMemberForm


@login_required
def home(request):
    """ A dispatch view based on user authorization"""
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('admin_dashboard'))
    else:
        return HttpResponseRedirect(reverse('user_dashboard'))


@login_required
def user_dashboard(request):
    """ User dashboard """
    title = _('User dashboard')
    members = User.objects.all()
    return render_to_response(
        'dashboard/user.html',
        context_instance=RequestContext(
            request,
            {'title': title,
             'members': members,}
            )
        )


@login_required
def admin_dashboard(request):
    """ Administrator dashboard  """
    title = _('Admin dashboard')
    members = User.objects.all()
    form = AddMemberForm()
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render_to_response(
        'dashboard/admin.html',
        context_instance=RequestContext(
            request,
            {'title': title,
             'members': members,
             'form': form,}
            )
        )
