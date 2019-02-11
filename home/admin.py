from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Property #this line added
admin.site.register(Property)#this line added