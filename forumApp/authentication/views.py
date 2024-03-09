
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_page(request):
    form = forms.SignUpForm()
    message = ''
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            message = 'Invalid form.'
    return render(request, 'authentication/signup.html', {'form': form, 'message': message})

@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('account')
    else:
        form = forms.UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'authentication/changeprofile.html', context)

