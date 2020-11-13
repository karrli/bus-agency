from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CharField
from django.db.models import PROTECT

from buses.models import Route
from buses.models import Passenger


class Travel(Model):
    route = ForeignKey(
        Route, 
        on_delete=PROTECT, 
    )

    seat = CharField(max_length=5)

    passenger = ForeignKey(
        Passenger, 
        on_delete=PROTECT,
    )

    class Meta:
        app_label = 'buses'