from django.db.models import Model
from django.db.models import CharField
from django.db.models import TextField

class Journey(Model):
    origin = CharField(max_length=30)
    destination = CharField(max_length=30)
    description = TextField()

    class Meta:
        app_label = 'buses'
    def __str__(self):
        return f'{self.origin} ({self.destination})'