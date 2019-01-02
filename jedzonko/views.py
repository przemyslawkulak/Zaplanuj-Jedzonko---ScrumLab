import random
from datetime import datetime

from django.shortcuts import render
from django.views import View

from jedzonko.models import Plan, Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)

# nie działała próba uruchomienia wyświetlania szablonu za pomocą pętli

def carousel(request):
    recipes = random.sample(list(Recipe.objects.all()), 3)
    return render(request, 'index.html', {'first': recipes[0], 'second': recipes[1], 'last': recipes[2]})


def main_page(request):
    ctx_plan = Plan.objects.all().count()
    ctx_recipe = Recipe.objects.all().count()
    return render(request, "dashboard.html", {'plans_count': ctx_plan, 'recipe_count': ctx_recipe})


def recipe_list(request):
    return render(request, "recipes.html")


def recipe_add(request):
    if request.method == "POST":
        return render(request, 'app-add-recipe.html')
    elif request.method == "GET":
        return render(request, 'app-add-recipe.html')
