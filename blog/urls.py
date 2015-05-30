from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns(
    '',
    url(r'^lists', lists.as_view(), name="lists"),
    url(r'^forms', PostFormView.as_view(), name="forms"),
)
