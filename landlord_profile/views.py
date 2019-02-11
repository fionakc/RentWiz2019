from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def landlord_profile(request):
    return render(request, 'landlord_profile.html')