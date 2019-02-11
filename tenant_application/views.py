from django.shortcuts import render, get_object_or_404
from PIL import Image
from property_listing.models import Property;
from property_listing.models import Listing;


def apply(request, id):
    listing = Listing.objects.get(id=id)
    context = {'listing': listing,
               }
    return render(request, 'apply.html', context)


def addTenants(request, id):
    qset = Property.objects.get(id=id)
    context = {'queryset': qset,
               }
    return render(request, 'addTenants.html', context)


def addMoreT(request):
    return render(request, 'addMoreT.html')


def conditions(request):
    return render(request, 'conditions.html')


def confirmation(request):
    return render(request, 'confirmation.html')

