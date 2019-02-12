from django.shortcuts import get_object_or_404, redirect, render
from UserManagement.models import Contact
from property_listing.models import Landlord

# Create your views here.

def index(request):
    landlord_id = 3
    # if (request.user):
    #     contact = Contact.objects.filter(user=request.user)
    #     landlord_id = Landlord.objects.filter(contact=contact).id
    #     if (landlord_id):


    context = {'landlord_id': landlord_id}
    return render(request, 'index.html', context)
