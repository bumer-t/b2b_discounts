# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from discounts.views import agreements_calendar, main_view


urlpatterns = patterns('',
    (r'^$',                         main_view),
    url(r'^agreements/calendar/$',  agreements_calendar,    name='agreements_calendar'),
)
