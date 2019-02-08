from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/tenant', views.register_tenant, name='register_tenant'),
    path('register/landlord', views.register_landlord, name='register_landlord'),
    path('register/propertymanager', views.register_propertymanager, name='register_propertymanager'),
]