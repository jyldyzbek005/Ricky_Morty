from rest_framework import serializers
from .models import Location, Character, Epizode


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class EpizodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epizode
        fields = '__all__'