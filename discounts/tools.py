# -*- coding: utf-8 -*-
from django.db.models import Q
from discounts.consts.request_params import MAP_Q_AGR_CAL


def get_query(slug, cleaned_data):
    values_list = cleaned_data[slug]
    key = '%s__%s' % (MAP_Q_AGR_CAL[slug], 'in' if len(values_list) > 1 else 'exact')
    value = values_list if len(values_list) > 1 else values_list[0]
    return Q(**{key: value})
