from django.shortcuts import get_object_or_404, redirect, render


def landlord_profile(request):
    return render(request, 'landlord_profile.html')