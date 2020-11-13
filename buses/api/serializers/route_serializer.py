from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Route

class RouteSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Route
        fields = [
        'id',
        'journey',
        'schedule',
        'bus',
        'driver'
        ]
