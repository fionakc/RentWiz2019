from django.urls import path

from . import views
urlpatterns=[
    path('apply/', views.apply, name='apply'),
    path('addTenants/', views.addTenants, name='addTenants'),
    path('conditions/', views.conditions, name='conditions'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('addMoreT/', views.addMoreT, name='addMoreT'),
    path('tenant-profile/<int:tenant_id>/', views.updateTenantProfile, name='tenant_profile'),
]