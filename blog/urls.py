from django.conf.urls import include, url 
from django.contrib import admin

from .views import (blog_list,
	blog_detail,
	blog_create,
	blog_delete,
	blog_update)

urlpatterns = [
    url(r'^$', blog_list, name='list'),
    url(r'^create/$', blog_create),
    url(r'^(?P<slug>[\w-]+)/$', blog_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$', blog_delete),
    url(r'^(?P<slug>[\w-]+)/update/$', blog_update),
]