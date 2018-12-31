from django.core.validators import MinValueValidator, MaxValueValidator
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


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, \t{self.description}, \tcreated {self.created}'


class DayName(models.Model):
    day_type = models.CharField(max_length=16)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.day_type} : {self.order}'


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=255)
    order = models.IntegerField()
    day_name_id = models.ForeignKey(DayName, on_delete=models.CASCADE, related_name="dayname")
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plan")
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")


def __str__(self):
    return f'{self.meal_name}, order: {self.order}'


class Page(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}, \t{self.description}'
