# -*- coding: utf-8 -*-
from django.contrib import admin
from discounts.models import Negotiator, Country, Company, Agreement, Period


class CommonAdmin(admin.ModelAdmin):
    list_per_page = 20


class NegotiatorAdmin(CommonAdmin):
    list_display    = ('username', 'email')
    search_fields   = ['username', 'email']


class CountryAdmin(CommonAdmin):
    list_display    = ('code', 'name', 'created', 'changed')
    search_fields   = ['code', 'name']


class CompanyAdmin(CommonAdmin):
    list_display    = ('name', 'country', 'created', 'changed')
    search_fields   = ['name', 'country__code']
    raw_id_fields   = ('country',)


class PeriodInline(admin.StackedInline):
    model = Period
    extra = 0
    exclude = ('is_last',)


class AgreementAdmin(CommonAdmin):
    list_display    = ('company', 'created', 'changed', 'negotiator', 'date_start', 'date_end', 'export_turnover',
                       'import_turnover')
    raw_id_fields   = ('company', 'negotiator',)
    list_filter     = ('company', 'negotiator')
    search_fields   = ['company__country__code', 'company__country__name']
    inlines         = [PeriodInline]


class PeriodAdmin(CommonAdmin):
    list_display    = ('created', 'changed', 'agreement', 'date_start', 'date_end', 'status', 'is_last')
    list_filter     = ('status', 'is_last',)
    raw_id_fields   = ('agreement',)
    exclude         = ('is_last',)


admin.site.register(Negotiator, NegotiatorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Period, PeriodAdmin)
