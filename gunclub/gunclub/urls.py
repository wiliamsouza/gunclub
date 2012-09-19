from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from dashboard.views import home, user_dashboard, admin_dashboard
from member.views import add_member, edit_member

urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', home, name='home'),
    url(r'^dashboard/user/$', user_dashboard, name='user_dashboard'),
    url(r'^dashboard/admin/$', admin_dashboard, name='admin_dashboard'),
    url(r'^member/add/$', add_member, name='add_member'),
    url(r'^member/edit/(?P<member_id>\d+)/$', edit_member, name='edit_member'),
    (r'^search/', include('haystack.urls')),
)
urlpatterns += staticfiles_urlpatterns()
