from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from core.forms import UserLoginForm


def frontpage(request):
    """For rendering frontpage"""
    return render(request, 'core/frontpage.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:frontpage')
        else:
            return render(request, 'core/signup.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('core:frontpage')


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    return redirect(request.GET['next'])
                except:
                    return redirect('core:frontpage')
            else:
                return render(request, 'core/login.html', {'form': form})
        else:
            return render(request, 'core/login.html', {'form': form})
    form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})
