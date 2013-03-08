from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^listem/$', 'listem.views.index'),
	url(r'^listem/(?P<lists_id>\d+)/$', 'listem.views.detail'),
	url(r'^listem/(?P<lists_id>\d+)/fresh/$', 'listem.views.fresh'),

    # # Examples:
    # url(r'^$', 'foodstar.views.home', name='home'),
    # url(r'^foodstar/', include('foodstar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)