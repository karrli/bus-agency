from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import PROTECT


from buses.models import Journey
from buses.models import Schedule
from buses.models import Bus
from buses.models import Driver

class Route(Model):
    journey = ForeignKey(
        Journey,
        on_delete=PROTECT,
    )

    schedule = ForeignKey(
        Schedule,
        on_delete=PROTECT,
    )

    bus = ForeignKey(
        Bus,
        on_delete=PROTECT,
    )

    driver = ForeignKey(
        Driver,
        on_delete=PROTECT,
    )
    
    class Meta:
        app_label = 'buses'
