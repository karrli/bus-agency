from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Bus

class BusSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Bus
        fields = [
        'id',
        'plate',
        'capacity'
        ] 
