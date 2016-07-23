# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET


@require_GET
@csrf_exempt
def agreements_calendar(request):
    params = {
        's': 's',
    }
    return HttpResponse(json.dumps(params), 'application/json')
