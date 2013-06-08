from django.conf.urls import patterns, include, url

from testApp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testWeb.views.home', name='home'),
    # url(r'^testWeb/', include('testWeb.testWeb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^testApp/', include('testApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
