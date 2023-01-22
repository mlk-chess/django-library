from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.

def register(request):
    if not request.user.is_anonymous:
        return redirect("register" if request.user.role == 'client_role' else "bookseller_route")

    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if user.role == 'client_role':
                return redirect(settings.LOGIN_REDIRECT_URL + '/client')
            elif user.role == 'bookseller_role':
                return redirect(settings.LOGIN_REDIRECT_URL + '/bookseller')
    return render(request, "register/index.html", context={'form': form})
