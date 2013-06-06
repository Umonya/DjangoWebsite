from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'umonya.app.main.views.home', name='home'),
    url(r'^about/$', 'umonya.app.main.views.about'),
    url(r'^resources/$', 'umonya.app.main.views.resources'),
    url(r'^registration/$', 'umonya.app.main.views.registration'),
    url(r'^contact/$', 'umonya.app.main.views.contact'),
    url(r'^course/$', 'umonya.app.main.views.course'),
    
    # url(r'^umonya/', include('umonya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
