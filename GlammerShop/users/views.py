from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('main:main')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)

def signin(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signin.html', context)

def recovery(request):
    context = {}
    return render(request, 'users/recovery.html', context)

def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect('main:index')