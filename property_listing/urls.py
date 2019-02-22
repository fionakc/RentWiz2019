from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('landlord_profile/<int:landlord_id>', views.landlord_profile, name='landlord_profile'),
    path('property_manager_profile/<int:property_manager_id>', views.property_manager_profile,
         name='property_manager_profile'),
    path('add_property_for_landlord/<int:landlord_id>', views.add_property_for_landlord,
         name='add_property_for_landlord'),
    path('add_listing/<int:property_id>', views.add_listing, name='add_listing'),
]