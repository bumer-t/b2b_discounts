# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import patterns, include, url


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('discounts.urls')),
)
