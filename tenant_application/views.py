from django.shortcuts import render

# Create your views here.
def apply(request):
    return render(request, 'apply.html')

def addTenants(request):
    return render(request, 'addTenants.html')

def conditions(request):
    return render(request, 'conditions.html')