from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form

    else:  # get request
        form = RegistrationForm()
        context['register_form'] = form

    return render(request, 'musicapp/admin/registration.html', context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('admin')
        else:
            context['login_form'] = form
    else:
        form = UserLoginForm()
        context['login_form'] = form

    return render(request, 'musicapp/admin/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

