from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('search_listings/', views.search_listings, name='search_listings'),
    # path('property_details/<int:id>', views.show_property_details, name='show_property_details'),
]