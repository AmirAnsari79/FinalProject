from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserLoginForm, UserRegistrationForm
from .models import User


def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, ("وارد شدید"), 'success')
                return redirect('core:home')
            else:
                messages.error(request, "یوزر یا رمز اشتباه است", 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})


def UserLogout(request):
    logout(request)
    messages.success(request, "logout", 'success')
    return redirect('core:home')


def UserRegister(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password'])
            user.save()
            messages.success(request, "", 'success')
            return redirect('core:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})
