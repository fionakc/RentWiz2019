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
        max_length=80,
        required=False
    )
    address_line3 = forms.CharField(
        max_length=80,
        required=False
    )
    home_phone = forms.CharField(
        max_length=20,
        required=False
    )
    work_phone = forms.CharField(
        max_length=20,
        required=False
    )
    mobile_phone = forms.CharField(
        max_length=20,
        required=False
    )
    #photo = forms.ImageField()
    password1 = forms.CharField(
        max_length=20,
    )


class PropertyManagerCreationForm(ContactCreationForm):
    pass

    def save(self):
        data = self.cleaned_data
        user = RegisteredUser(username=data['registered_username'])

        user.set_password(data["password1"])
        user.save()

        contact = Contact(user=user,
                          name=data['name'],
                          email=data['email'],
                          address_line1=data['address_line1'],
                          )

        contact.address_line2 = data['address_line2']
        contact.address_line3 = data['address_line3']
        contact.home_phone = data['home_phone']
        contact.work_phone = data['work_phone']
        contact.mobile_phone = data['mobile_phone']
        contact.save()

        property_manager = PropertyManager(contact=contact)
        property_manager.save()

        return user



class TenantCreationForm(ContactCreationForm):
    pass

    def save(self):
        data = self.cleaned_data
        user = RegisteredUser(username=data['registered_username'])

        user.set_password(data["password1"])
        user.save()

        contact = Contact(user=user,
                          name=data['name'],
                          email=data['email'],
                          address_line1=data['address_line1'],
                          )

        contact.address_line2 = data['address_line2']
        contact.address_line3 = data['address_line3']
        contact.home_phone = data['home_phone']
        contact.work_phone = data['work_phone']
        contact.mobile_phone = data['mobile_phone']
        contact.save()

        tenant = Tenant(contact=contact,
                        legal_name=data['name'],
                        is_18_plus=True,)  #using these two values to get the form to also save to tenants, should have own fields on form
                                            #or be created when filling out tenant profile.
                                            #only an issue atm because creating a tenant and these are required fields, so must be filled on construction
        tenant.save()
        return user

class LandlordCreationForm(ContactCreationForm):

    tenancy_services_id = forms.CharField(
        required=False
    )

    def save(self):
        data = self.cleaned_data
        user = RegisteredUser(username=data['registered_username'])
        user.set_password(data["password1"])
        user.save()

        contact = Contact(user=user,
                          name=data['name'],
                          email=data['email'],
                          address_line1=data['address_line1'],
                          )

        contact.address_line2 = data['address_line2']
        contact.address_line3 = data['address_line3']
        contact.home_phone = data['home_phone']
        contact.work_phone = data['work_phone']
        contact.mobile_phone = data['mobile_phone']
        contact.save()

        landlord = Landlord(contact=contact,
                        is_first_timer=True, )
        landlord.tenancy_services_id = data['tenancy_services_id']
        landlord.save()

        return user