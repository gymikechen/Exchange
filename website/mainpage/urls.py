from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'', views.index_page, name='index_page'),
)



