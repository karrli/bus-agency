from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Travel

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = [
        'id',
        'route',
        'seat',
        'passenger'
        ]  