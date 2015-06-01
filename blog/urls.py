from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns(
    '',
    url(r'^user', UserList.as_view(), name="user"),
    url(r'^$', StoreUser.as_view(), name="store"),
    url(r'^getuser/$', GetUser.as_view(), name='getuser'),
    url(r'^token/$', TokenRequest.as_view(), name='token'),
)
