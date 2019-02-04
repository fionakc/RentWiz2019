from django.conf.urls import url, include
from .views import PropertyListView, PropertyDetailView

urlpatterns = [
    url('', PropertyListView.as_view()),
    url('<pk>', PropertyDetailView.as_view()),
]
