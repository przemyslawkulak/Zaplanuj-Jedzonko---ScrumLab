from django.core.validators import MinValueValidator
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    preparation_time = models.IntegerField(MinValueValidator(1))
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.ingredients}, {self.description}'

