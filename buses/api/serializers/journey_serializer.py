from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Journey

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = [
        'id',
        'origin',
        'destination',
        'description',
        ]  