from django.contrib import admin
from buses.models import *

# Register your models here.

class BusesAdmin (admin.ModelAdmin):
    pass
admin.site.register(Bus, BusesAdmin)
class DriversAdmin (admin.ModelAdmin):
    pass
admin.site.register(Driver, DriversAdmin)
class SchedulesAdmin (admin.ModelAdmin):
    pass
admin.site.register(Schedule, SchedulesAdmin)
class RoutesAdmin (admin.ModelAdmin):
    pass
admin.site.register(Route, RoutesAdmin)
class PassengersAdmin (admin.ModelAdmin):
    pass
admin.site.register(Passenger, PassengersAdmin)
class JourneysAdmin (admin.ModelAdmin):
    pass
admin.site.register(Journey, JourneysAdmin)

class TravelsAdmin (admin.ModelAdmin):
    pass
admin.site.register(Travel, TravelsAdmin)
