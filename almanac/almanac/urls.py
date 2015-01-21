from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^export/(?P<state>\w+)/$', 'xml_dump.views.home', name='home'),
    url(r'^check/$', 'xml_dump.views.check_states', name='check_states'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
