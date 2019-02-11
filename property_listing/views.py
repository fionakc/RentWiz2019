from django.shortcuts import get_object_or_404, redirect, render
from .forms import LandlordProfileForm
from .models import Landlord, Listing, Property, PropertyManager
from UserManagement.models import Contact


def landlord_profile(request, landlord_id):
    landlord = Landlord.objects.get(id=landlord_id)
    contact = Contact.objects.get(landlord=landlord)
    initial_data = {'name': contact.name,
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
        form = LandlordProfileForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'landlord_profile.html', context)
