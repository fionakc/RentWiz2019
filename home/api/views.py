from rest_framework.generics import ListAPIView, RetrieveAPIView
from home.models import Property
from .serializers import PropertySerializer


class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyDetailView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
