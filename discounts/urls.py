# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from discounts.views import agreements_calendar, main_view, agreements_calendar_by_is_last


urlpatterns = patterns('',
    (r'^$',                         main_view),
    url(r'^agreements/calendar/$',  agreements_calendar,    name='agreements_calendar'),


    url(r'^agreements/calendar__is_last/$',  agreements_calendar_by_is_last,    name='agreements_calendar_by_is_last'),
)
