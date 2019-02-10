from django.shortcuts import render

# Create your views here.
def apply(request):
    return render(request, 'apply.html')

def addTenants(request):
    return render(request, 'addTenants.html')

def addMoreT(request):
    return render(request, 'addMoreT.html')

def conditions(request):
    return render(request, 'conditions.html')

def confirmation(request):
    return render(request, 'confirmation.html')