from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

@login_required
def home(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('admin_dashboard'))
    else:
        return HttpResponseRedirect(reverse('user_dashboard'))


@login_required
def user_dashboard(request):
    return render_to_response(
        'user/dashboard.html',
        context_instance=RequestContext(
            request,
            {'a': '',
             'b': '',}
            )
        )


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render_to_response(
        'admin/dashboard.html',
        context_instance=RequestContext(
            request,
            {'a': '',
             'b': '',}
            )
        )
