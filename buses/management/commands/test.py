from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
from django.db.models import Count
from django.db.models import Avg

from buses.models import Bus, Driver, Passenger, Schedule, Route, Travel, Journey

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.test()
        
    def test(self):
        journeys = Journey.objects.all()
        routes = Route.objects.values('journey_id').annotate(routes_per_journey=Count('schedule_id'))
        passengers_by_journey = Route.objects.values('journey_id').annotate(passengers = Count('travel'))


        dict_avg = {}
        for route in routes:
            route_list = list(route.values())
            passengers_by_journey = Route.objects.values('journey_id').annotate(passengers = Count('travel')).filter(journey_id = route_list[0])
            journeys = Journey.objects.filter(id = route_list[0])
            journeys_list = str(list(journeys))
            print(journeys_list)
            passengers_query_list = list(passengers_by_journey)
            passengers_list = list(passengers_query_list[0].values())
            passengers_int = int(passengers_list[1])
            routes_int = int(route_list[1])
            average = passengers_int/routes_int
            dict_avg[journeys_list] = average
        print(dict_avg)

        
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.test()

    def test(self):
        routes = Route.objects.all()
 
        # dict_avg= {}
        responses = []
        for route in routes:
           
            buses = Bus.objects.filter(id = route.bus_id)
            buses_list = str(list(buses))
            journeys = Journey.objects.filter(id = route.journey_id)
            journeys_list = str(list(journeys))
            all_journeys = route.journey
            r = Route.objects.get(id=route.id)
            #Filtro de porcentaje  
            if  r.travel_set.count()*10 >= 10:
                queries = r.travel_set.all().values('route_id').annotate(seats_occupied=Count('seat'))
                for querie in queries:
                    r = Route.objects.get(id=route.id)
                    responses.append(buses_list)
                    responses.append(journeys_list)
                    responses.append(querie)
                    data ={
                        'ruta': route.journey,
                        'datos de la ruta': querie
                    } 
                    # print(data)
        print(responses)       
        



