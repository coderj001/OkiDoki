from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('core:login'))
def okirprofile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }
    return render(request, 'okirprofile/okirprofile.html', context=context)


@login_required(login_url=reverse_lazy('core:login'))
def follow_okir(request, username):
    user = get_object_or_404(User, username=username)
    request.user.okirprofile.follows.add(user.okirprofile)
    return redirect("okirprofile:okirprofile", username=username)


@login_required(login_url=reverse_lazy('core:login'))
def unfollow_okir(request, username):
    user = get_object_or_404(User, username=username)
    request.user.okirprofile.follows.remove(user.okirprofile)
    return redirect("okirprofile:okirprofile", username=username)
