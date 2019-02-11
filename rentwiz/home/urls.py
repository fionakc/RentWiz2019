from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test-page', views.test, name='test'),
    path('Property/<int:id>', views.show_artifact_details, name='show_artifact_details'),
]