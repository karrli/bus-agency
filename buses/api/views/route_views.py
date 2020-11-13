from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Count, Avg
from buses.models import (Route,
                          Journey, 
                          Bus)
from buses.api.serializers.route_serializer import RouteSerializer

class RouteList(APIView):
    """
    List all routes, or create a new route.
    """
    def get(self, request, format=None):
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class RouteListAveragePassengers(APIView):

    def get(self, request):
    
        journeys = Journey.objects.all()
        routes = Route.objects.values('journey_id').annotate(routes_per_journey=Count('schedule_id'))
        passengers_by_journey = Route.objects.values('journey_id').annotate(passengers = Count('travel'))

        dict_avg = {}
        for route in routes:
            route_list = list(route.values())
#             passengers_by_journey = Route.objects.values('journey_id').annotate(passengers = Count('travel')).filter(journey_id = route_list[0])
            journeys = Journey.objects.filter(id = route_list[0])
            journeys_list = str(list(journeys))
            passengers_query_list = list(passengers_by_journey)
            passengers_list = list(passengers_query_list[0].values())
            passengers_int = int(passengers_list[1])
            routes_int = int(route_list[1])
            average = passengers_int/routes_int
            dict_avg[journeys_list] = average
            

        return Response(dict_avg, status=HTTP_200_OK)

class RouteListBusesCapacity(APIView):

    def get(self, request):
        routes = Route.objects.all()
        responses = []

        for route in routes:
            dict_avg = {}
            buses = Bus.objects.filter(id = route.bus_id)
            buses_list = str(list(buses))
            journeys = Journey.objects.filter(id = route.journey_id)
            journeys_list = str(list(journeys))
            r = Route.objects.get(id=route.id)
            #Filtro de porcentaje, 30% en este caso  
            if  r.travel_set.count()*10 >= 30:
                queries = r.travel_set.all().values('route_id').annotate(seats_occupied=Count('seat'))
                for querie in queries:
                    r = Route.objects.get(id=route.id)
                    responses.append(buses_list)
                    responses.append(journeys_list)
                    responses.append(querie)

        return Response(responses, status=HTTP_200_OK)
    """
    Option to return either from data using Jsonreponse or from response as a list
    """                    
                    # data = {
                    #     'autobus': buses_list,
                    #     'trayecto': journeys_list,
                    #     'asientos vendidos por ruta': querie
                    # } 
                    # return JsonResponse({'data': data}, status=HTTP_200_OK)        


class RouteDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Route.objects.get(pk=pk)
        except Route.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        route = self.get_object(pk)
        serializer = RouteSerializer(route)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        route = self.get_object(pk)
        serializer = RouteSerializer(route, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        route = self.get_object(pk)
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)