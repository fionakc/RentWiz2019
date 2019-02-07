from django.contrib import admin
from .models import Landlord, Listing, Property, PropertyManager

admin.site.register(Landlord)
admin.site.register(Listing)
admin.site.register(Property)
admin.site.register(PropertyManager)
