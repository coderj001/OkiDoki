import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from feed.models import Oki, Like
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def api_add_oki(request):
    """ Added body to dbs when client request """
    data = json.loads(request.body)
    body = data['body']

    oki = Oki.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
def api_add_like(request):
    data = json.loads(request.body)
    oki_id = data['oki_id']

    if not Like.objects.filter(oki_id=oki_id).filter(created_by=request.user).exists():
        like = Like.objects.create(oki_id=oki_id, created_by=request.user)
    json_response = {'success': True}
    return JsonResponse(json_response)
