from django.conf.urls import patterns, url

urlpatterns = patterns('foodstar.views', 
	url(r'^$', 'index'),
	url(r'^(?P<foodlist_id>)\d+)/$', 'detail'),
	url(r'^(?P<foodlist_id>)\d+)/items/$', 'items'),
	#url(r'^(?P<foodlist_id>)\d+)/
	)
