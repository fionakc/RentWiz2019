from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RegisteredUser


class RegisteredUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = RegisteredUser
        fields = ('username', 'first_name', 'last_name', 'email',)


class RegisteredUserChangeForm(UserChangeForm):

    class Meta:
        model = RegisteredUser
        fields = ('username', 'first_name', 'last_name', 'email',)
