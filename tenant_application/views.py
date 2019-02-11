from django.shortcuts import render
from property_listing.models import Property;

# Create your views here.
def apply(request, id):
    qset = Property.objects.get(id=id)
    context = {'queryset': qset,
               }
    return render(request, 'apply.html', context)

def addTenants(request):
    return render(request, 'addTenants.html')

def addMoreT(request):
    return render(request, 'addMoreT.html')

def conditions(request):
    return render(request, 'conditions.html')

def confirmation(request):
    return render(request, 'confirmation.html')