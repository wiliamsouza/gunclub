"""
Invoice views for gunclub
"""

import datetime
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import (HttpResponseRedirect,
                         HttpResponseForbidden,
                         HttpResponse)

from  gunclub import settings

from member.models import Profile
from invoice.models import Invoice
from invoice.forms import EditInvoiceForm
from invoice import pdf


@login_required
def invoice(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    open_invoices = Invoice.objects.filter(is_paid=False).count()
    paid_invoices = Invoice.objects.filter(is_paid=True).count()
    return render_to_response(
        'invoice/invoice.html',
        {'open_invoices': open_invoices,
         'paid_invoices': paid_invoices},
        context_instance=RequestContext(request)
    )


@login_required
def member_invoice(request, member_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    member = get_object_or_404(Profile, id=member_id)
    invoices = []
    year = datetime.date.today().year
    membership = member.date_membership.month
    for month in range(membership, 13):
        due_date = datetime.date(year, month, member.invoice_due_day)
        invoice, created = Invoice.objects.get_or_create(
            user=member.user,
            due_date=due_date,
            value=settings.INVOICE_VALUE)
        invoices.append(invoice)
    return render_to_response(
        'invoice/list.html',
        {'invoices': invoices,
         'member': member},
        context_instance=RequestContext(request)
    )


@login_required
def edit_invoice(request, invoice_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if invoice_id:
        invoice = get_object_or_404(Invoice, id=invoice_id)
        form = EditInvoiceForm(instance=invoice)
    if request.method == 'POST':
        form = EditInvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save()
            return HttpResponseRedirect(
                reverse('member_invoice', kwargs={'member_id': invoice.user.id}))
    return render_to_response(
    'invoice/edit.html',
    {'form': form,
     'invoice_id': invoice_id},
    context_instance=RequestContext(request)
    )


@login_required
def print_invoice_booklet(request, member_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    profile = Profile.objects.get(pk=member_id)
    invoices = Invoice.objects.filter(is_paid=False, user=profile.user)
    user = profile.user
    pdf_file = pdf.generate_invoice_booklet_pdf(invoices, user, profile)
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % (
        user.get_full_name())
    response.write(pdf_file)
    return response


@login_required
def print_invoice(request, invoice_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    invoice = get_object_or_404(Invoice, id=invoice_id)
    profile = invoice.user.profile
    user = invoice.user
    pdf_file = pdf.generate_invoice_pdf(invoice.due_date, invoice.value,
                                        user, profile)
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s_%s.pdf' % (
        user.get_full_name(), invoice.due_date)
    response.write(pdf_file)
    return response


@login_required
def send_invoice(request, invoice_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    invoice = get_object_or_404(Invoice, id=invoice_id)
    profile = invoice.user.profile
    user = invoice.user
    pdf_file = pdf.generate_invoice_pdf(invoice.due_date,
                                        invoice.value,
                                        user, profile)
    email = EmailMessage(subject=settings.EMAIL_SUBJECT,
                         body=settings.EMAIL_BODY,
                         from_email=settings.EMAIL_FROM,
                         to=[user.email])
    email.attach('%s_%s.pdf' % ( user.get_full_name(), invoice.due_date),
                 pdf_file, 'application/pdf')
    email.send(fail_silently=False)
    return render_to_response(
        'invoice/email.html',
        context_instance=RequestContext(request)
    )
