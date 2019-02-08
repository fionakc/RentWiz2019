from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_tenant', views.register_tenant, name='register_tenant'),
    path('register_landlord', views.register_landlord, name='register_landlord'),
    path('register_propertymanager', views.register_propertymanager, name='register_propertymanager'),
]