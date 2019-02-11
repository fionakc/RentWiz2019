from django.contrib.auth.models import AbstractUser
from django.db import models


class RegisteredUser(AbstractUser):

    # This is the list of fields, other than username and password,
    # (which are always required) that are required to be displayed at
    # registration.
    # Removing this may cause problems when using Django's
    # createsuperuser command.
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
        blank=True,
        null=True,
        on_delete=models.SET_NULL   # assume we want to retain the data
    )

    name = models.CharField(
        max_length=80, default=''
    )

    email = models.EmailField()

    address_line1 = models.CharField(
        max_length=80, default=''
    )

    address_line2 = models.CharField(
        max_length=80, blank=True
    )

    address_line3 = models.CharField(
        max_length=80, blank=True
    )

    home_phone = models.CharField(
        max_length=20, blank=True
    )

    work_phone = models.CharField(
        max_length=20, blank=True
    )

    mobile_phone = models.CharField(
        max_length=20, blank=True
    )

    #photo = models.ImageField(blank=True)

    def __str__(self):
        return 'Contact: ' + self.name
