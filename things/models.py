from django.db import models

class Things(models.Model):
    name = models.CharField()

    description = models.TextField()

    quantity = models.IntegerField()
