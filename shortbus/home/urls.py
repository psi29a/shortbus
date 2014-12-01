from django.conf.urls import *

from shortbus.home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/about/$', views.about, name='about'),
)
