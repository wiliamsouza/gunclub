from django.conf.urls import patterns, url
from django.views.generic import DetailView
from django.views.generic.dates import (DayArchiveView, MonthArchiveView,
                                        YearArchiveView)

from invoice.models import Invoice
from invoice.views import (member_invoice, edit_invoice, print_invoice,
                           print_invoice_booklet, send_invoice)


urlpatterns = patterns(
    '',
    url(r'^$',
        YearArchiveView.as_view(template_name='invoice/year.html',
                                date_field='due_date',
                                model=Invoice),
        name='invoice'),
    url(r'^month/$',
        MonthArchiveView.as_view(template_name='invoice/month.html',
                                 date_field='due_date',
                                 model=Invoice),
        name='invoice_month'),
    url(r'^day/$',
        DayArchiveView.as_view(template_name='invoice/day.html',
                               date_field='due_date',
                               model=Invoice),
        name='invoice_day'),
    url(r'^(?P<member_id>\d+)/$', member_invoice, name='member_invoice'),
    url(r'^edit/(?P<invoice_id>\d+)/$', edit_invoice, name='edit_invoice'),
    url(r'^print/(?P<invoice_id>\d+)/$', print_invoice, name='print_invoice'),
    url(r'^print/booklet/(?P<member_id>\d+)/$', print_invoice_booklet,
        name='print_invoice_booklet'),
    url(r'^send/(?P<invoice_id>\d+)/$', send_invoice, name='send_invoice'),
)
