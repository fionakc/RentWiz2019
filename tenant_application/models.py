from django.db import models
from django.utils import timezone
from property_listing.models import Listing
from UserManagement.models import Contact


class Tenant(models.Model):
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        # think about blank and null
    )

# Add fields for other relevant info for tenant role
    # Fields from 2018 are below
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_token = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return 'Tenant ' + self.contact.user.get_username()


class Reference(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    referee = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT
    )

    # Add other fields for reference

    def __str__(self):
        return 'Reference for ' + str(self.tenant) + ' by ' + str(self.referee)


class Application(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.PROTECT
    )

    lead_tenant = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT
    )

    co_tenants = models.ManyToManyField(Tenant)

    start_date_request = models.DateField(blank=True)
    duration_request = models.CharField(max_length=80, blank=True)
    comments = models.TextField(blank=True)
    # Below should perhaps be in Agreement; not here
    tcd_acceptance = models.BooleanField(null=True)

    def __str__(self):
        return 'Application by ' + str(self.lead_tenant) + ' for ' + str(self.listing)
