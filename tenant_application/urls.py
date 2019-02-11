from django.urls import path

from . import views
urlpatterns=[
    path('apply/<int:id>', views.apply, name='apply'),
    path('addTenants/<int:id>', views.addTenants, name='addTenants'),
    path('conditions/<int:id>', views.conditions, name='conditions'),
    path('confirmation/<int:id>', views.confirmation, name='confirmation'),
    path('addMoreT/<int:id>', views.addMoreT, name='addMoreT'),

]