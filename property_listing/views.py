from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import (AddListingForm, AddPropertyForLandlordForm, PostForm, LandlordProfileForm,
                    PropertyManagerProfileForm)
from .models import Landlord, Listing, Property, PropertyManager
from UserManagement.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'create_listing.html', {'form': form})


def landlord_profile(request, landlord_id):
    landlord = Landlord.objects.get(id=landlord_id)
    contact = Contact.objects.get(landlord=landlord)
    initial_landlord_data = {'name': contact.name,
                    'email': contact.email,
                    'address_line1': contact.address_line1,
                    'address_line2': contact.address_line2,
                    'address_line3': contact.address_line3,
                    'home_phone': contact.home_phone,
                    'work_phone': contact.work_phone,
                    'mobile_phone': contact.mobile_phone,
                    'tenancy_services_id': landlord.tenancy_services_id,
                    'is_first_timer': landlord.is_first_timer
                    }

    properties = list(Property.objects.filter(landlord=landlord))

    if request.method == 'POST':
        form = LandlordProfileForm(request.POST)
        if form.is_valid() and form.has_changed():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.address_line1 = form.cleaned_data['address_line1']
            contact.address_line2 = form.cleaned_data['address_line2']
            contact.address_line3 = form.cleaned_data['address_line3']
            contact.home_phone = form.cleaned_data['home_phone']
            contact.work_phone = form.cleaned_data['work_phone']
            contact.mobile_phone = form.cleaned_data['mobile_phone']
            landlord.tenancy_services_id = form.cleaned_data['tenancy_services_id']
            landlord.is_first_timer = form.cleaned_data['is_first_timer']
            contact.save()
            landlord.save()
    else:
        form = LandlordProfileForm(initial=initial_landlord_data)

    context = {'form': form, 'properties': properties}
    return render(request, 'landlord_profile.html', context)


def property_manager_profile(request, property_manager_id):
    property_manager = PropertyManager.objects.get(id=property_manager_id)
    contact = Contact.objects.get(property_manager=property_manager)
    initial_property_manager_data = {'name': contact.name,
                    'email': contact.email,
                    'address_line1': contact.address_line1,
                    'address_line2': contact.address_line2,
                    'address_line3': contact.address_line3,
                    'home_phone': contact.home_phone,
                    'work_phone': contact.work_phone,
                    'mobile_phone': contact.mobile_phone,
                    }

    properties = list(Property.objects.filter(property_manager=property_manager))

    if request.method == 'POST':
        form = PropertyManagerProfileForm(request.POST)
        if form.is_valid() and form.has_changed():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.address_line1 = form.cleaned_data['address_line1']
            contact.address_line2 = form.cleaned_data['address_line2']
            contact.address_line3 = form.cleaned_data['address_line3']
            contact.home_phone = form.cleaned_data['home_phone']
            contact.work_phone = form.cleaned_data['work_phone']
            contact.mobile_phone = form.cleaned_data['mobile_phone']
            contact.save()
            # Statement below is redundant right now, because there
            # actually is nothing to save for the PropertyManager
            # specifically in the current code.
            property_manager.save()
    else:
        form = PropertyManagerProfileForm(initial=initial_property_manager_data)

    context = {'form': form, 'properties': properties}
    return render(request, 'property_manager_profile.html', context)


def add_property_for_landlord(request, landlord_id):
    landlord = get_object_or_404(Landlord, id=landlord_id)
    property = Property.objects.create(landlord=landlord,
                                       bedrooms=0,
                                       tenant_capacity=0)
    # Note this always creates a new property when the page is called.
    # We should do something better, but ugly works for now.

    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddPropertyForLandlordForm(instance=property)

    context = {'form': form}
    return render(request, 'add_property_for_landlord.html', context)



def add_listing(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    listing = Listing.objects.create(property=property,
                                     start_date=timezone.now())
    # Note this always creates a new listing when the page is called.
    # We should do something better, but ugly works for now.

    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddListingForm(instance=listing)

    context = {'form': form}
    return render(request, 'add_listing.html', context)
