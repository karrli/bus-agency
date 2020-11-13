from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
        'id',
        'departure',
        'arrival'
        ]
