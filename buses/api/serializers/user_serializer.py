from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import (Driver, 
                            Route, 
                            Bus, 
                            Passenger) 

class UserSerializer(serializers.ModelSerializer):
    drivers = serializers.PrimaryKeyRelatedField(many=True, queryset=Driver.objects.all())
    routes = serializers.PrimaryKeyRelatedField(many=True, queryset=Route.objects.all())
    buses = serializers.PrimaryKeyRelatedField(many=True, queryset=Bus.objects.all())
    passengers = serializers.PrimaryKeyRelatedField(many=True, queryset=Passenger.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'drivers', 'routes', 'buses', 'passengers']
