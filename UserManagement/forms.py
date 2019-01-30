from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'organization')


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'organization')
