from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import RegisteredUserCreationForm, PropertyManagerCreationForm, TenantCreationForm, LandlordCreationForm




def register(request):
    if request.method == 'POST':
        form = RegisteredUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisteredUserCreationForm()
    #return render(request, 'register.html', {'form': form})
    return render(request, 'register.html')


def register_tenant(request):

    if request.method == 'POST':
        form = TenantCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = TenantCreationForm()
    return render(request, 'register_tenant.html', {'form': form})


def register_landlord(request):

    if request.method == 'POST':
        form = LandlordCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = LandlordCreationForm()
    return render(request, 'register_landlord.html', {'form': form})


def register_propertymanager(request):
    #return render(request, 'register_propertymanager.html')

    if request.method == 'POST':
        form = PropertyManagerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = PropertyManagerCreationForm()

    return render(request, 'register_propertymanager.html', {'form': form})



