from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Driver
        fields = [
        'id',    
        'name',
        'lastname',
        'identity_no'    
        ]