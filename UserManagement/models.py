from django.contrib.auth.models import AbstractUser
from django.db import models


class RegisteredUser(AbstractUser):
    # Next 3 fields are in AbstractUser class.
    # The main feature added in their overrides here is the addition
    # of a help_text.
    first_name = models.CharField(
        max_length=30,
        blank=True,
        help_text=''
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        help_text=''
    )
    email = models.EmailField(
        max_length=150,
        blank=True,
        help_text=''
    )

    # This is the list of fields, other than username and password,
    # (which are always required) that are required to be displayed at
    # registration.
    REQUIRED_FIELDS = ['email']

    # add additional fields below here
    is_guest = models.BooleanField(
        default=False,
        help_text='Is the user a Guest user?',
    )

    def __str__(self):
        return 'User: ' + self.get_username()


class Contact(models.Model):
    user = models.OneToOneField(
        RegisteredUser,
        on_delete=models.SET_NULL   # assume we want to retain the data
    )

    address = models.CharField(
        max_length=120,
    )

    mobile = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return 'Contact record for ' + str(self.user)
