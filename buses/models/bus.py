from django.db.models import Model
from django.db.models import CharField
from django.db.models import IntegerField

class Bus(Model):
    plate = CharField(max_length=10)
    capacity = IntegerField(default=10)

    class Meta:
        app_label = 'buses'

    def __str__(self):
        return str(self.plate)