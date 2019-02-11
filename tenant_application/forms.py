from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import request

from .models import Contact
from property_listing.models import Landlord, PropertyManager
from tenant_application.models import Tenant, Reference, Application
from django import forms

#form to enter DOB, smoking, pets
class TenantProfile_part1_Form(forms.Form):

    date_of_birth = forms.DateField(
        required=False
    )

    is_smoker = forms.BooleanField(
        required=False
    )
    has_pets = forms.BooleanField(
        required=False
    )

    #current_user = request.user

    def save(self, request):
        data = self.cleaned_data
        # forms.current_user = request.user
        tenant = request.user
        tenant.date_of_birth = data['date_of_birth']
        tenant.is_smoker = data['is_smoker']
        tenant.has_pets = data['has_pets']


        # tenant = Tenant(legal_name= "bob",
        #                 is_18_plus=True,
        #     date_of_birth = data['date_of_birth'],
        #     is_smoker = data['is_smoker'],
        #     has_pets = data['has_pets'])
        tenant.save()


    # date_of_birth = forms.DateField()
    #
    # is_smoker = forms.BooleanField()
    #
    # has_pets = forms.BooleanField()

# class PropertyManagerCreationForm(ContactCreationForm):
#     pass
#
#     def save(self):
#         data = self.cleaned_data
#         user = RegisteredUser(username=data['registered_username'])
#
#         user.set_password(data["password1"])
#         user.save()
#         contact = Contact(user=user,
#                           name=data['name'],
#                           email=data['email'],
#                           address_line1=data['address_line1'],
#                           address_line2=data['address_line2'],
#                           address_line3=data['address_line3'],
#                           home_phone=data['home_phone'],
#                           work_phone=data['work_phone'],
#                           mobile_phone=data['mobile_phone'],
#                           #photo=data['photo'],
#         )
#         contact.save()
#         property_manager = PropertyManager(contact=contact)
#         property_manager.save()

# class ContactCreationForm(forms.Form):
#     registered_username = forms.CharField(
#         max_length=80
#     )
#     name = forms.CharField(
#         max_length=80
#     )
#     email = forms.EmailField()
#     address_line1 = forms.CharField(
#         max_length=80
#     )
#     address_line2 = forms.CharField(
#         max_length=80,
#     )
#     address_line3 = forms.CharField(
#         max_length=80,
#     )
#     home_phone = forms.CharField(
#         max_length=20,
#     )
#     work_phone = forms.CharField(
#         max_length=20,
#     )
#     mobile_phone = forms.CharField(
#         max_length=20,
#     )
#     #photo = forms.ImageField()
#     password1 = forms.CharField(
#         max_length=20,
#     )
