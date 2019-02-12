from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import request


from .models import Contact
from property_listing.models import Landlord, PropertyManager
from tenant_application.models import Tenant, Reference, Application
from django import forms

#form to enter DOB, smoking, pets
class TenantProfile_part1_Form(forms.Form):

    date_of_birth = forms.DateField(
        required=False,
        #help_text='yyyy-mm-dd'
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
    )

    is_smoker = forms.BooleanField(
        required=False
    )
    has_pets = forms.BooleanField(
        required=False
    )

    id_type_choices = (('1','Drivers License'),('2','Passport'),('3','Other'))

    identification_type = forms.ChoiceField(
        # max_length=20,
        required=False,
        choices=id_type_choices,
        widget=forms.RadioSelect,
    )


    identification_number = forms.CharField(
        # It doesn't have to be a number.
        # For a drivers license you could add classification too
        max_length=40,
        required=False,
    )

    vehicle_registration = forms.CharField(
        max_length=10,
        required=False,
    )
    vehicle_make_and_model = forms.CharField(
        max_length=80,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Please enter'}),
        # label=_(u'Text'),
    )


    is_first_timer = forms.BooleanField(required=False)
    has_children = forms.BooleanField(required=False)

    #free text area:
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(),
    )


    #current_user = request.user

    def save(self,instance):
        data = self.cleaned_data
        # forms.current_user = request.user
        tenant = instance
        tenant.date_of_birth = data['date_of_birth']
        tenant.is_smoker = data['is_smoker']
        tenant.has_pets = data['has_pets']

        #tenant.identification_type = data['identification_type']
        tenant.identification_number = data['identification_number']
        tenant.vehicle_registration = data['vehicle_registration']
        tenant.vehicle_make_and_model = data['vehicle_make_and_model']
        tenant.is_first_timer = data['is_first_timer']
        tenant.has_children = data['has_children']
        tenant.comments = data['comments']


