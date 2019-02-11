from django.urls import path

from . import views
urlpatterns=[
    path('apply/<int:id>', views.apply, name='apply'),
    path('addTenants/<int:id>', views.addTenants, name='addTenants'),
    path('conditions/', views.conditions, name='conditions'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('addMoreT/', views.addMoreT, name='addMoreT'),

]