from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import DetailView

from dashboard.views import home, user_dashboard, admin_dashboard
from member.views import add_member, edit_member

from member.models import Profile

urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', home, name='home'),
    url(r'^dashboard/user/$', user_dashboard, name='user_dashboard'),
    url(r'^dashboard/admin/$', admin_dashboard, name='admin_dashboard'),
    url(r'^member/add/$', add_member, name='add_member'),
    url(r'^member/$', edit_member, name='member'),
    url(r'^member/edit/(?P<member_id>\d+)/$', edit_member, name='edit_member'),
    url(r'^member/detail/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Profile,
            context_object_name='member',
            template_name='member/detail.html'),
        name='detail_member'),
##    url(r'^invoice/$', invoice_dashboard, name='invoice_dashboard'),
##    url(r'^invoice/(?P<member_id>\d+)/$', user_invoice, name='user_invoice'),
    url(r'^search/', include('haystack.urls')),
)
urlpatterns += staticfiles_urlpatterns()
