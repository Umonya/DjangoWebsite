from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main_app.views.home', name='home'),
    url(r'^about/$', 'main_app.views.about'),
    url(r'^resources/$', 'main_app.views.resources'),
    url(r'^registration/$', 'main_app.views.registration'),
    url(r'^contact/$', 'main_app.views.contact'),
    url(r'^course/$', 'main_app.views.course'),
    
    # url(r'^umonya/', include('umonya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
