from django.db import models
from django.utils import timezone
from UserManagement.models import Contact


class Landlord(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        # think about blank and null
    )

    tenancy_services_id = models.CharField(
        max_length=8, blank=True
    )

    is_first_timer = models.BooleanField(
        null=True
    )

# Add fields for other relevant info for landlord role

    def __str__(self):
        return 'Landlord: ' + self.contact.name


class PropertyManager(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        # think about blank and null
    )

    # Add fields for other relevant info for property manager role

    def __str__(self):
        return 'PropertyManager: ' + self.contact.name


class Property(models.Model):
    landlord = models.ForeignKey(
        Landlord,
        null=True,
        on_delete=models.SET_NULL
        # think about blank and null
    )

    property_manager = models.ForeignKey(
        PropertyManager,
        null=True,
        on_delete=models.SET_NULL
        # think about blank and null
    )

    tenancy_services_id = models.CharField(
        max_length=8, blank=True
    )

    room_number = models.CharField(max_length=4, blank=True)
    unit_number = models.CharField(max_length=4, blank=True)
    house_number = models.CharField(max_length=4, blank=True)
    building_name = models.CharField(max_length=80, blank=True)
    street_name = models.CharField(max_length=80, default='')
    suburb = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    region = models.CharField(max_length=50, blank=True)

    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(blank=True, null=True)
    tenant_capacity = models.IntegerField()
    car_spaces = models.IntegerField(blank=True, null=True)

    dwelling_type = models.CharField(
        max_length=20,
        choices=[('House/Townhouse', 'House/Townhouse'),
                 ('Apartment', 'Apartment'),
                 ('Room', 'Room'),
                 ('Boarding house room', 'Boarding house room'),
                 ('Bedsit/Flat', 'Bedsit/Flat'),
                 ],
        blank = True
    )
    description = models.TextField(blank=True)

    has_unit_title = models.BooleanField(default=False)

    # Jelle: can be amended to Image table if we want to enable more
    # than 1 picture per property.
    property_picture = models.ImageField(blank=True)

    school_zone = models.CharField(max_length=80, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    has_rental_wof = models.BooleanField(null=True)
    # insulation information; probably needs to be separate table
    # utilities information ???
    # chattels information should probably be in Listing table

    # Following comments copied from 2018 model in GitHub
    # Latitude, longitude fields kept out for version 1
    # - Plan to add these at a later date
    # - Addition will allow implementation of a mapping feature
    # longitude = Column(Numeric(precision=10, scale=7))
    # latitude = Column(Numeric(precision=10, scale=7))

    def __str__(self):
        return 'Property at ' + self.street_name  + ' in ' + self.city


class Listing(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        # think about blank and null
    )

    start_date = models.DateField()
    duration = models.CharField(max_length=80, blank=True)
    # We could split above into a duration unit and quantity, e.g.
    # IntegerField for quantity and CharField for unit. We could then
    # have choices such as week, month, year for the unit.
    price = models.DecimalField(max_digits=9,
                                decimal_places=2,
                                default='0')
# Following field names were in 2018 ERM diagram.
    # price_low = models.DecimalField(max_digits=9, decimal_places=2)
    # price_high = models.DecimalField(max_digits=9, decimal_places=2)
    payment_frequency = models.CharField(max_length=20, default='')

    description = models.TextField(blank=True)

    # terms and conditions
    # duties
    # listing_status

    def __str__(self):
        return 'Listing for ' + str(self.property)  + ' starting on ' + str(self.start_date)
