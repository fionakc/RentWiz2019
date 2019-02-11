from django.urls import path

from . import views

urlpatterns = [
    path('landlord_profile/<int:landlord_id>', views.landlord_profile, name='landlord_profile'),
]
