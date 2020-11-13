from django.db.models import Model
from django.db.models import DateTimeField
from django.utils import timezone


class Schedule(Model):
    departure = DateTimeField(
        default=timezone.now,
    )
    arrival = DateTimeField(
        default=timezone.now,
    )
    
    class Meta:
        app_label = 'buses'
    def __str__(self):
        return f'{self.departure} ({self.arrival})'