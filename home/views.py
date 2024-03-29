from django.shortcuts import get_object_or_404, redirect, render
from property_listing.models import Property;
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'index.html')



# This pulls queryset to manage.py console in Django
def test(request):
    qset = Property.objects.all()
    print(qset)
    args = qset
    return render(request, 'test-page.html', {'queryset': args})



# VIEW
def show_artifact_details(request, id):

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



