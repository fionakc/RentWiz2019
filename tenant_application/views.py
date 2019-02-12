from django.shortcuts import render
from django.views.generic.edit import UpdateView

from tenant_application.models import Tenant
from UserManagement.models import Contact
from .forms import TenantProfile_part1_Form
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


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

