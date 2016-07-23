# -*- coding: utf-8 -*-
import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.decorators.http import require_GET
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from discounts.consts.request_params import REQ_COUNTRY, REQ_COMPANY, REQ_NEGOTIATOR
from discounts.decorators.request_decorators import api_view_500
from discounts.forms import AgreementsCalendarForm
from discounts.models import Agreement
from discounts.tools import get_query


def main_view(request):
    params = {}
    request_context = RequestContext(request)
    response = render_to_response('index.html', params, context_instance=request_context)
    return response


@require_GET
@api_view_500()
@csrf_exempt
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
    agreements = Agreement.objects.prefetch_related('period_set').filter(query)
    for agreement in agreements:
        last_period = agreement.last_period
        result.setdefault(last_period.date_end.year, [0]*12)
        result[last_period.date_end.year][last_period.date_end.month-1] += 1
    return HttpResponse(json.dumps(result), 'application/json')


# from django.db import connection
# from django.db.models import Sum, Count
# truncate_date = connection.ops.date_trunc_sql('month', 'date_end')
# qs = Period.objects.extra({'month':truncate_date})
# report = qs.values('month').annotate(Count('pk')).order_by('month')
# print report
