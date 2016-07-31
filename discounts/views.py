# -*- coding: utf-8 -*-
import json
import datetime as dt

from django.http.response import HttpResponse
from django.db import connection
from django.db.models import Q, Count, Max
from django.views.decorators.http import require_GET
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from discounts.consts.request_params import REQ_COUNTRY, REQ_COMPANY, REQ_NEGOTIATOR
from discounts.decorators.request_decorators import api_view_500
from discounts.forms import AgreementsCalendarForm
from discounts.models import Agreement, Period
from discounts.tools import get_query


def main_view(request):
    params = {}
    request_context = RequestContext(request)
    response = render_to_response('index.html', params, context_instance=request_context)
    return response


@require_GET
@api_view_500()
def agreements_calendar(request):
    input_data = request.GET.dict()
    form = AgreementsCalendarForm(input_data)
    if not form.is_valid():
        return HttpResponse(json.dumps({'status': False, 'message': form.errors}), 'application/json')

    cleaned_data = form.cleaned_data
    query = Q(period__is_last=True)
    if cleaned_data.get(REQ_COMPANY):
        query &= get_query(REQ_COMPANY, cleaned_data)
    if cleaned_data.get(REQ_COUNTRY):
        query &= get_query(REQ_COUNTRY, cleaned_data)
    if cleaned_data.get(REQ_NEGOTIATOR):
        query &= get_query(REQ_NEGOTIATOR, cleaned_data)

    result = {}
    agreements = Agreement.objects.filter(query).annotate(p_date_end=Max('period__date_end'))
    for agreement in agreements:
        date_end = agreement.p_date_end
        result.setdefault(date_end.year, [0]*12)
        result[date_end.year][date_end.month-1] += 1
    return HttpResponse(json.dumps(result), 'application/json')


@require_GET
@api_view_500()
def agreements_calendar_by_is_last(request):
    input_data = request.GET.dict()
    form = AgreementsCalendarForm(input_data)
    if not form.is_valid():
        return HttpResponse(json.dumps({'status': False, 'message': form.errors}), 'application/json')

    cleaned_data = form.cleaned_data
    query = Q(is_last=True)
    if cleaned_data.get(REQ_COMPANY):
        query &= get_query(REQ_COMPANY, cleaned_data, is_last=True)
    if cleaned_data.get(REQ_COUNTRY):
        query &= get_query(REQ_COUNTRY, cleaned_data, is_last=True)
    if cleaned_data.get(REQ_NEGOTIATOR):
        query &= get_query(REQ_NEGOTIATOR, cleaned_data, is_last=True)

    result = {}
    truncate_date = connection.ops.date_trunc_sql('month', '%s_%s.date_end' % (Period._meta.app_label.lower(), Period.__name__.lower()))
    last_periods = Period.objects.select_related('agreement').filter(query).extra(select={'month': truncate_date}).values('month').annotate(Count('pk'))
    for last_period in last_periods:
        date_end = dt.datetime.strptime(last_period['month'], '%Y-%m-%d')
        result.setdefault(date_end.year, [0]*12)
        result[date_end.year][date_end.month-1] += last_period['pk__count']
    return HttpResponse(json.dumps(result), 'application/json')
