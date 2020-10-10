from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from feed.models import Oki


@login_required(login_url=reverse_lazy('core:login'))
def feed(request):
    userids = [request.user.id]
    for okir in request.user.okirprofile.follows.all():
        userids.append(okir.okir.id)
    okis = Oki.objects.filter(created_by_id__in=userids)
    return render(request, 'feed/index.html', {'okis': okis})
