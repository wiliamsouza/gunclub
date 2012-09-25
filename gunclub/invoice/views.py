"""
Invoice views for gunclub
"""

from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden

from member.models import Profile
from invoice.models import Invoice

@login_required
def member_invoice(request, member_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    member = get_object_or_404(Profile, id=member_id)
    invoices = Invoice.objects.filter(user=member)
    return render_to_response(
    'invoice/list.html',
    {'invoices': invoices,
     'member': member},
    context_instance=RequestContext(request)
    )

##@login_required
##def create_invoice(request, member_id):
##    if not request.user.is_staff:
##        return HttpResponseForbidden()
##    return render_to_response(
##    'invoice/member.html',
##    {'invoices': invoices,
##     'member': member},
##    context_instance=RequestContext(request)
##    )
