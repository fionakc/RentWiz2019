from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import RegisteredUserCreationForm


def register(request):
    if request.method == 'POST':
        form = RegisteredUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisteredUserCreationForm()
    return render(request, 'register.html', {'form': form})


def register_tenant(request):
    return render(request, 'register_tenant.html')


def register_landlord(request):
    return render(request, 'register_landlord.html')


def register_propertymanager(request):
    return render(request, 'register_propertymanager.html')



