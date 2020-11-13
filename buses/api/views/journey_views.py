from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Count, Avg
from buses.models import Journey
from buses.api.serializers.journey_serializer import JourneySerializer

class JourneyList(generics.ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class JourneyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]        
