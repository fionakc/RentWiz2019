from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # original below is broken
    # path('search_listings/', views.search_listings, name='search_listings'),
    # path('search_listings/', views.index, name='search_listings'),
    # path('property_details/<int:id>', views.show_property_details, name='show_property_details'),
    path('search_listings/', views.search_listings, name='search_listings'),
    path('property_details/<int:id>', views.show_property_details, name='show_property_details'),
]