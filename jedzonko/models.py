from django.db import models


# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateField()
