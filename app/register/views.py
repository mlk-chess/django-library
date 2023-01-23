from django.shortcuts import render
from . import forms
from django.contrib.auth import login
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            role = form.cleaned_data.get('role')
            if role == 'client':
                return redirect('index')
            elif role == 'bookseller':
                return redirect('bookseller_index')
    else:
        form = forms.RegisterForm()
    return render(request, 'register/index.html', {'form': form})
