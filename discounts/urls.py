# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from discounts.views import agreements_calendar


urlpatterns = patterns('',
    url(r'^agreements/calendar/$',  agreements_calendar,    name='agreements_calendar'),
)
