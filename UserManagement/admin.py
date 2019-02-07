from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisteredUserCreationForm, RegisteredUserChangeForm
from .models import Contact, RegisteredUser


class RegisteredUserAdmin(UserAdmin):
    add_form = RegisteredUserCreationForm
    form = RegisteredUserChangeForm
    model = RegisteredUser
    list_display = ['username', 'email', 'is_guest']


admin.site.register(Contact)
admin.site.register(RegisteredUser)
# admin.site.register(RegisteredUserAdmin)
