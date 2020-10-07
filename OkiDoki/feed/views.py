from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy('core:login'))
def feed(request):
    return render(request, 'feed/index.html', {})
