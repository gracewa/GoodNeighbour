from rest_framework import serializers
from ..models import Neighbourhood, Business, EmergencyService, Profile
from django.contrib.auth.models import User



class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('id', 'name', 'location', 'admin')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email')