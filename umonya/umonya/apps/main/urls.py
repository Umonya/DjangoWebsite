from django.conf.urls import patterns, include, url

#~ Creating the App importable
urlpatterns	= patterns('',
	url(r'^$', 'umonya.apps.main.views.home', name='home'),
	url(r'^about/$', 'umonya.apps.main.views.about'),
	url(r'^resources/$', 'umonya.apps.main.views.resources'),
	url(r'^registration/$', 'umonya.apps.main.views.registration'),
	url(r'^contact/$', 'umonya.apps.main.views.contact'),
	url(r'^course/$', 'umonya.apps.main.views.course'),
)
