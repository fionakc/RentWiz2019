from django import forms

class LandlordProfileForm(forms.Form):
    name = forms.CharField(
        max_length=80
    )

    email = forms.EmailField(
        max_length=120, required=False,)

    address_line1 = forms.CharField(
        max_length=80
    )

    address_line2 = forms.CharField(
        max_length=80, required=False,
    )

    address_line3 = forms.CharField(
        max_length=80, required=False,
    )

    home_phone = forms.CharField(
        max_length=20, required=False,
    )

    work_phone = forms.CharField(
        max_length=20, required=False,
    )

    mobile_phone = forms.CharField(
        max_length=20, required=False,
    )

    tenancy_services_id = forms.CharField(
        max_length=8, required=False,
    )

    is_first_timer = forms.NullBooleanField(

    )

    def save(self):
        pass