from rest_framework.viewsets import ModelViewSet
from .models import Location, Character, Epizode
from .serializers import LocationSerializer, CharacterSerializer, EpizodeSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class EpizodeViewSet(ModelViewSet):
    queryset = Epizode.objects.all()
    serializer_class = EpizodeSerializer





