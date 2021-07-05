from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Person(models.Model):
    iin = models.CharField(max_length=200)
    age = models.IntegerField(default=5)

    def __str__(self):
        return self.iin

