# -*- coding: utf-8 -*-
from django.contrib import admin
from discounts.models import Negotiator, Country, Company, Agreement, Period


class CommonAdmin(admin.ModelAdmin):
    list_per_page = 20


class NegotiatorAdmin(CommonAdmin):
    list_display    = ('username', 'email')
    search_fields   = ['username', 'email']


class CountryAdmin(CommonAdmin):
    list_display    = ('id', 'name', 'created', 'changed')
    search_fields   = ['id', 'name']


class CompanyAdmin(CommonAdmin):
    list_display    = ('name', 'country', 'created', 'changed')
    search_fields   = ['name', 'country__id']
    raw_id_fields   = ('country',)


class AgreementAdmin(CommonAdmin):
    list_display    = ('company', 'date_start', 'date_end', 'negotiator', 'export_turnover', 'import_turnover')
    raw_id_fields   = ('company', 'negotiator',)


class PeriodAdmin(CommonAdmin):
    list_display    = ('agreement', 'date_start', 'date_end', 'status')
    list_filter     = ('status',)
    raw_id_fields   = ('agreement',)


admin.site.register(Negotiator, NegotiatorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Period, PeriodAdmin)
