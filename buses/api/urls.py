from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from buses.api.views import (bus_views, 
                            driver_views, 
                            journey_views, 
                            passenger_views, 
                            route_views, 
                            schedule_views, 
                            travel_views, 
                            user_views) 

urlpatterns = [
    path('drivers/api/', driver_views.DriverList.as_view()),
    path('drivers/api/<int:pk>/', driver_views.DriverDetail.as_view()),
    path('routes/api/', route_views.RouteList.as_view()),
    path('routes/api/average', route_views.RouteListAveragePassengers.as_view()),
    path('routes/api/capacity', route_views.RouteListBusesCapacity.as_view()),
    path('routes/api/<int:pk>/', route_views.RouteDetail.as_view()),
    path('buses/api/', bus_views.BusList.as_view()),
    path('buses/api/<int:pk>/', bus_views.BusDetail.as_view()),
    path('schedules/api/', schedule_views.ScheduleList.as_view()),
    path('schedules/api/<int:pk>/', schedule_views.ScheduleDetail.as_view()),
    path('passengers/api/', passenger_views.PassengerList.as_view()),
    path('passengers/api/<int:pk>/', passenger_views.PassengerDetail.as_view()),
    path('journeys/api/', journey_views.JourneyList.as_view()),
    path('journeys/api/<int:pk>/', journey_views.JourneyDetail.as_view()),
    path('travels/api/', travel_views.TravelList.as_view()),
    path('travels/api/<int:pk>/', travel_views.TravelDetail.as_view()),
    path('users/', user_views.UserList.as_view()),
    path('users/<int:pk>/', user_views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)