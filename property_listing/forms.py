from django import forms

from .models import Property

class PostForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('room_number', 'unit_number', 'bedrooms', 'tenant_capacity')