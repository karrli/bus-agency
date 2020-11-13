from django.db.models import Model
from django.db.models import CharField


# Create your models here.
class Driver(Model):
    name = CharField(max_length=20)
    lastname = CharField(max_length=20)
    identity_no = CharField(max_length=20)
    
    class Meta:
        app_label = 'buses'
    def __str__(self):
        return f'{self.name} ({self.lastname})'