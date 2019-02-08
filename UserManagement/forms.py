from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RegisteredUser, Contact
from property_listing.models import Landlord, PropertyManager
from tenant_application.models import Tenant
from django import forms


class RegisteredUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = RegisteredUser
        fields = ('username', 'first_name', 'last_name', 'email',)


class RegisteredUserChangeForm(UserChangeForm):

    class Meta:
        model = RegisteredUser
        fields = ('username', 'first_name', 'last_name', 'email',)


class ContactCreationForm(forms.Form):

    registered_username = forms.CharField(
        max_length=80
    )
    name = forms.CharField(
        max_length=80
    )
    email = forms.EmailField()
    address_line1 = forms.CharField(
        max_length=80
    )
    address_line2 = forms.CharField(
        max_length=80
    )
    address_line3 = forms.CharField(
        max_length=80
    )
    home_phone = forms.CharField(
        max_length=20
    )
    work_phone = forms.CharField(
        max_length=20
    )
    mobile_phone = forms.CharField(
        max_length=20
    )
    photo = forms.ImageField()


class LandlordCreationForm(forms.Form):

    user = forms.CharField(
        max_length=80
    )
    name = forms.CharField(
        max_length=80
    )
    email = forms.EmailField()
    address_line1 = forms.CharField(
        max_length=80
    )
    address_line2 = forms.CharField(
        max_length=80
    )
    address_line3 = forms.CharField(
        max_length=80
    )
    home_phone = forms.CharField(
        max_length=20
    )
    work_phone = forms.CharField(
        max_length=20
    )
    mobile_phone = forms.CharField(
        max_length=20
    )
    photo = forms.ImageField()

class PropertyManagerCreationForm(ContactCreationForm):

    pass

    def save(self):
        data = self.cleaned_data
        user = RegisteredUser(username=data['registered_username'], password1=data['password1'],
            password2=data['password2'])
        user.save()
        contact = Contact(user=user,
        name=data['name'],
                        email=data['email'],
                          address_line1=data['address_line1'],
        address_line2 = data['address_line2'],
        address_line3 = data['address_line3'],
                          home_phone=data['home_phone'],
                          work_phone=data['work_phone'],
                          mobile_phone=data['mobile_phone'],
                          photo=data['photo'],

                          )
        contact.save()
        property_manager = PropertyManager(contact=contact)
        property_manager.save()




