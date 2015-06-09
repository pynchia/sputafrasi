from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
#import sputafrasi
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sputafrasi.views.home', name='home'),
    url(r'^update_status$', 'sputafrasi.views.update_status', name="update_status"),
    url(r'^editpref$', 'sputafrasi.views.editpref', name="editpref"),
    url(r'^setpref$', 'sputafrasi.views.setpref', name="setpref"),
    ('^alldone$', direct_to_template, {
        'template': 'all_done.html'
    }),
    ('^prefdone$', direct_to_template, {
        'template': 'pref_done.html'
    }),
#    ('^privacy/$', direct_to_template, {
#        'template': 'privacy.html'
#    }),
#    ('^helpdesk/$', direct_to_template, {
#        'template': 'helpdesk.html'
#    }),
#    ('^terms/$', direct_to_template, {
#        'template': 'terms.html'
#    }),
    # url(r'^sputafrasi/', include('sputafrasi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
