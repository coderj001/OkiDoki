from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from feed.models import Oki
from django.contrib.auth.models import User
# from django.core.paginator import Paginator


@login_required(login_url=reverse_lazy('core:login'))
def feed(request):
    userids = [request.user.id]
    for okir in request.user.okirprofile.follows.all():
        userids.append(okir.okir.id)
    okis = Oki.objects.filter(created_by_id__in=userids)
    for oki in okis:
        likes = oki.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            oki.liked = True
        else:
            oki.liked = False
    # TODO: Added paginator
    # paginator = Paginator(okis, 5)
    # page_num = request.GET.get("page", 1)
    # page_obj = paginator.get_page(page_num)
    # try:
    #         users = paginator.page(page)
    #     except PageNotAnInteger:
    #         users = paginator.page(1)
    #     except EmptyPage:
    #         users = paginator.page(paginator.num_pages)

    return render(request, 'feed/index.html', {'okis': okis})


@login_required(login_url=reverse_lazy('core:login'))
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        okirs = User.objects.filter(username__icontains=query)
    else:
        okirs = []

    context = {
        'query': query,
        'okirs': okirs,
    }
    return render(request, 'feed/search.html', context=context)
