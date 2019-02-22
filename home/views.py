from django.shortcuts import get_object_or_404, redirect, render
from UserManagement.models import Contact
from property_listing.models import Landlord
from property_listing.models import Property;
from property_listing.models import Listing;

# Create your views here.

# This was hardcoded for demonstration purposes
def index(request):
    landlord_id = 3
    # if (request.user):
    #     contact = Contact.objects.filter(user=request.user)
    #     landlord_id = Landlord.objects.filter(contact=contact).id
    #     if (landlord_id):


    context = {'landlord_id': landlord_id}
    return render(request, 'index.html', context)

# This pulls queryset to manage.py console in Django
def search_listings(request):
    listings = Listing.objects.all()
    return render(request, 'test-page.html', {'listings': listings})


# VIEW
def show_property_details(request, id):

    qset = Property.objects.get(id=id)
    print(qset)

    # if request.method == 'POST':
    #     artifact_form = ArtifactForm(request.POST, instance=artifact)
    #     link_form = ArtifactImageLinkForm(request.POST, instance=link)
    #     if all([artifact_form.is_valid(), link_form.is_valid()]):
    #         artifact_form.save()
    #         link_form.save()
    # else:
    #     artifact_form = ArtifactForm(instance=artifact)
    #     link_form = ArtifactImageLinkForm(instance=link)

    context = {'queryset': qset,
               }
    return render(request, 'Property.html', context)



