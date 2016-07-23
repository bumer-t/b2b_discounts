# -*- coding: utf-8 -*-
import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from discounts.models import Agreement


@require_GET
@csrf_exempt
def agreements_calendar(request):
    result = {}
    agreements = Agreement.objects.prefetch_related('period_set').filter(period__is_last=True)
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
