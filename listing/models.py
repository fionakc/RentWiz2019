from django.db import models
from django.utils import timezone
from UserManagement.models import Contact


class Landlord(models.Model):
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        # think about blank and null
    )

# Add fields for other relevant info for landlord role

    def __str__(self):
        return 'Landlord ' + self.contact.user.get_username()


class PropertyManager(models.Model):
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        # think about blank and null
    )

    # Add fields for other relevant info for property manager role

    def __str__(self):
        return 'PropertyManager ' + self.contact.user.get_username()


class Property(models.Model):
    landlord = models.ForeignKey(
        Landlord,
        on_delete=models.SET_NULL
        # think about blank and null
    )

    property_manager = models.ForeignKey(
        PropertyManager,
        on_delete=models.SET_NULL
        # think about blank and null
    )

    # Following fields copied from 2018 model in GitHub; this is not
    # identical to ERM from their report and presentation
    street_address = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    bathrooms = models.IntegerField()
    tenant_capacity = models.IntegerField()
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=50, blank=True)
    bedrooms = models.IntegerField()
    # Jelle: below should probably be DecimalField
    price = models.FloatField()
    # Latitude, longitude fields kept out for version 1
    # - Plan to add these at a later date
    # - Addition will allow implementation of a mapping feature
    # longitude = Column(Numeric(precision=10, scale=7))
    # latitude = Column(Numeric(precision=10, scale=7))
    date_added = models.DateField(default=timezone.now)
    # Jelle: why refer "sold" below?
    date_sold = models.DateField(blank=True, null=True)
    # Jelle: below should probably be ImageField
    property_picture = models.CharField(max_length=500, blank=True, null=True)

    # Jelle: Item below commented out for 2019 work
    # status = models.ForeignKey(
    #     PropertyStatus,
    #     related_name='property',
    #     default=DEFAULT_PROPERTY_STATUS,
    #     on_delete=models.CASCADE,
    #     null=True
    # )

    def __str__(self):
        return 'Property at ' + self.street_address


class Listing(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        # think about blank and null
    )

    # Following field names were in 2018 ERM diagram. Field types
    # are temporary assumptions now
    description = models.TextField()
    price_low = models.DecimalField()
    price_high = models.DecimalField()
    current_tenant_capacity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tenant_feedback = models.TextField()
    # listing_status

