# -*- coding: utf-8 -*-
from discounts.consts.request_params import REQ_COUNTRY, REQ_COMPANY, REQ_NEGOTIATOR
from django import forms
from django.core.exceptions import ValidationError


class AgreementsCalendarForm(forms.Form):
    country     = forms.CharField(min_length=1, max_length=255, required=False, help_text=u'country')
    negotiator  = forms.CharField(min_length=1, max_length=255, required=False, help_text=u'negotiator')
    company     = forms.CharField(min_length=1, max_length=255, required=False, help_text=u'company')

    def clean_country(self):
        return self.__clean_common(REQ_COUNTRY)

    def clean_company(self):
        return self.__clean_common(REQ_COMPANY)

    def clean_negotiator(self):
        return self.__clean_common(REQ_NEGOTIATOR)

    def __clean_common(self, slug):
        slug_data = self.cleaned_data[slug]
        if not slug_data:
            return []
        slugs = slug_data.split(',')
        result = []
        for c in slugs:
            if not c.isdigit():
                raise ValidationError(u'%s - only digit (1,2,3,4)' % slug)
            result.append(int(c))
        return result
