from django.shortcuts import render, get_object_or_404
from PIL import Image
from property_listing.models import Property;
from property_listing.models import Listing;

from tenant_application.models import Tenant
from UserManagement.models import Contact
from .forms import TenantProfile_part1_Form
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def apply(request, id):
    listing = Listing.objects.get(id=id)
    context = {'listing': listing,
               }
    return render(request, 'apply.html', context)


def addTenants(request, id):
    qset = Listing.objects.get(id=id)
    context = {'queryset': qset,
               }
    return render(request, 'addTenants.html', context)


def addMoreT(request, id):
    qset = Listing.objects.get(id=id)
    context = {'queryset': qset,
               }
    return render(request, 'addMoreT.html', context)


def conditions(request, id):
    qset = Listing.objects.get(id=id)
    context = {'queryset': qset,
               }
    return render(request, 'conditions.html', context)

def confirmation(request, id):
    listing = Listing.objects.get(id=id)
    context = {'listing': listing,
               }
    return render(request, 'confirmation.html', context)


def done(request, id):
    listing = Listing.objects.get(id=id)
    context = {'listing': listing,
               }
    return render(request, 'done.html', context)


def updateTenantProfile(request, tenant_id):
    contact = [x for x in Contact.objects.all() if request.user == x.user][0]
    tenant = [y for y in Tenant.objects.all() if contact == y.contact][0]

    initial_data = {
        #for every field, field name and field value
        # 'legal_name': tenant.legal_name,
        'date_of_birth': tenant.date_of_birth,
        'is_smoker': tenant.is_smoker,
        'has_pets': tenant.has_pets,

        'identification_number': tenant.identification_number,
        'vehicle_registration': tenant.vehicle_registration,
        'vehicle_make_and_model': tenant.vehicle_make_and_model,
        'is_first_timer': tenant.is_first_timer,
        'has_children': tenant.has_children,
    }
    if request.method == 'POST':
        form = TenantProfile_part1_Form(request.POST)
        if form.is_valid():
            # tenant.is_smoker = form.cleaned_data.get('is_smoker')
            # tenant.has_pets = form.cleaned_data.get('has_pets')
            #tenant.save()

            form.save(tenant)  # still need this??
    else:
        form = TenantProfile_part1_Form(initial=initial_data)

    context = {'contact': contact, 'tenant': tenant, 'form': form}
    return render(request, 'tenantProfile.html', context)

