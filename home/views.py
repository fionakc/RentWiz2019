from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def index(request):
    # landlord_id = 42
    # context = {'landlord_id': landlord_id}
    return render(request, 'index.html')
