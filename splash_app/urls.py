from django.conf.urls import patterns, include, url
from splash_app import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^$', views.index, name='index')
    )