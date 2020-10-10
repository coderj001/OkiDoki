import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from feed.models import Oki
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def api_add_oki(request):
    data = json.loads(request.body)
    body = data['body']

    oki = Oki.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})
