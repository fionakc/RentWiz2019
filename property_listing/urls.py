from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('landlord_profile/<int:landlord_id>', views.landlord_profile, name='landlord_profile'),
]