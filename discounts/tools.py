# -*- coding: utf-8 -*-
from django.db.models import Q
from discounts.consts.request_params import MAP_Q_AGR_CAL


def get_query(slug, cleaned_data, is_last=False):
    values_list = cleaned_data[slug]
    filed = 'agreement__%s' % MAP_Q_AGR_CAL[slug] if is_last else MAP_Q_AGR_CAL[slug]
    key = '%s__%s' % (filed, 'in' if len(values_list) > 1 else 'exact')
    value = values_list if len(values_list) > 1 else values_list[0]
    return Q(**{key: value})
