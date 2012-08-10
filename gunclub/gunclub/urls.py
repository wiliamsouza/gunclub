from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gunclub.views import home, user_dashboard, admin_dashboard


urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', home, name='home'),
    url(r'^dashboard/user/', user_dashboard, name='user_dashboard'),
    url(r'^dashboard/admin/', admin_dashboard, name='admin_dashboard'),
)
urlpatterns += staticfiles_urlpatterns()
