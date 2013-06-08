from django.conf.urls import patterns, url

from testApp import views

urlpatterns = patterns ('', 
    url(r'^$', views.index, name='index'),
    url(r'^pastie/(?P<pastie_id>\d+)/$', views.pastie, name='pastie'),
    url(r'^paste', views.paste, name='paste'),
)