from django.db import models
from django.utils import timezone
from property_listing.models import Listing
from UserManagement.models import Contact


class Tenant(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        # think about blank and null
    )

    # Should we have field(s) for legal address; or ForeignKey
    # reference to another Contact for address.

    legal_name = models.CharField(
        max_length=80,
        default=contact.name,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_18_plus = models.BooleanField()

    identification_type = models.CharField(
        max_length=20,
        blank=True,
        choices=[('Drivers License', 'Drivers License'),
                 ('Passport', 'Passport'),
                 ('Other', 'Other')],
    )
    identification_number = models.CharField(
        # It doesn't have to be a number.
        # For a drivers license you could add classification too
        max_length=40,
        blank=True,
    )

    vehicle_registration = models.CharField(
        max_length=10,
        blank=True,
    )
    vehicle_make_and_model = models.CharField(
        max_length=80,
        blank=True,
    )

    emergency_contact = models.ForeignKey(
        Contact,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    employer = models.ForeignKey(
        Contact,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    # References will be in the Reference table.

    is_first_timer = models.BooleanField(null=True)
    has_verified_id = models.BooleanField(default=False)
    is_verified_profile = models.BooleanField(default=False)
    is_background_checked = models.BooleanField(default=False)
    is_smoker = models.BooleanField(null=True)
    has_children = models.BooleanField(null=True)
    has_pets = models.BooleanField(null=True)
    comments = models.TextField(blank=True)

    rating = models.IntegerField(blank=True, null=True)

# Add fields for other relevant info for tenant role

    def __str__(self):
        return 'Tenant: ' + self.contact.name


class Reference(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    referee = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT
    )

    description = models.TextField(blank=True)
    # Add other fields for reference
    # E.g. reference type

    def __str__(self):
        return 'Reference for ' + str(self.tenant) + ' by ' + str(self.referee)


class Application(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.PROTECT
    )

    lead_tenant = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,
    )

    # Below commented out because of error message caused by having
    # ForeignKey as well as ManyToManyField  to same table
    # co_tenants = models.ManyToManyField(Tenant)

    start_date_request = models.DateField(blank=True)
    duration_request = models.CharField(max_length=80, blank=True)
    comments = models.TextField(blank=True)
    # Below should perhaps be in Agreement; not here
    has_accepted_tcd = models.BooleanField(null=True)

    def __str__(self):
        return 'Application by ' + str(self.lead_tenant) + ' for ' + str(self.listing)
