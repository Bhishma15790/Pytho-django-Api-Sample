
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    price = models.FloatField(max_length=5)
    

    def __str__(self) -> str:
        return self.name + ' ' + self.discription