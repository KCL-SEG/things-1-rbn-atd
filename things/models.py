from django.db import models
from django.db.models.Model import Model

class Things(Model):
    name = models.CharField()

    description = models.TextField()

    quantity = models.IntegerField()
