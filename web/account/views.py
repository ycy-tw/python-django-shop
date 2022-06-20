
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import (
    LogInForm,
    RegistrationForm,
)


def login_view(request):

    user = request.user
    if user.is_authenticated:
        return redirect('shop:home')

    context = {}
    if request.POST:
        form = LogInForm(request.POST)

        if form.is_valid():

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            login(request, user)

            return redirect('shop:home')

    else:
        form = LogInForm()

    context['form'] = form
    return render(request, "account/user/login.html", context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('shop:home')


def register_view(request):

    user = request.user
    if user.is_authenticated:
        return redirect('shop:home')

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:edit_user')
    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, 'account/user/register.html', context)
