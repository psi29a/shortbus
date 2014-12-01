from django.conf.urls import *

from shortbus.field import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
