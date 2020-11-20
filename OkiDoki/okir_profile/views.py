from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from okir_profile.forms import OkirProfileForm


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


@login_required(login_url=reverse_lazy('core:login'))
def followers(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
    }
    return render(request, 'okirprofile/followers.html', context=context)


@login_required(login_url=reverse_lazy('core:login'))
def follows(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
    }
    return render(request, 'okirprofile/follows.html', context=context)


@login_required(login_url=reverse_lazy('core:login'))
def editprofileview(request):
    if request.method == 'POST':
        form = OkirProfileForm(request.POST, request.FILES,
                               instance=request.user.okirprofile)
        if form.is_valid():
            form.save()
            return redirect(
                'okirprofile:okirprofile',
                username=request.user.username
            )
        else:
            return render(
                request,
                'okirprofile/editprofile.html',
                {'form': form, 'user': request.user}
            )
    else:
        form = OkirProfileForm(instance=request.user.okirprofile)
        return render(
            request,
            'okirprofile/editprofile.html',
            {'form': form, 'user': request.user}
        )
