from django.contrib import admin
from .models import Application, Reference, Tenant

admin.site.register(Application)
admin.site.register(Reference)
admin.site.register(Tenant)



