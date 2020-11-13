from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Passenger
        fields = [
        'id',
        'name',
        'lastname'
        ]