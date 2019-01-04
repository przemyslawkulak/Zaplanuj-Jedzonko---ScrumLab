import random
from datetime import datetime

from django.core.paginator import Paginator
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
    b = Recipe.objects.all().order_by('-votes', '-created')
    paginator = Paginator(b, 50)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    return render(request, "recipes.html", {'all_recipes': a})


def recipe_add(request):
    if request.method == "POST":
        return render(request, 'app-add-recipe.html')
    elif request.method == "GET":
        return render(request, 'app-add-recipe.html')


def recipe_detail(request, id):
    recipe_details = []
    recipe = Recipe.objects.all().filter(id=id)
    for value in recipe:
        recipe_details.append({"name": value.name, 'ingredients': value.ingredients,
                               'description': value.description, 'preparation_time': value.preparation_time,
                               'votes': value.votes})
        return render(request, "recipe-details.html", {'recipe_details': recipe_details})


def contact_link(request):
    return render(request, "contact.html")


def about_link(request):
    return render(request, "about.html")


def index_link(request):
    return render(request, "index.html")


def plan_list(request):
    b = Plan.objects.all().order_by('name')
    paginator = Paginator(b, 2)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    return render(request, "app-schedules.html", {'all_plans': a})


def plan_add(request):
    if request.method == "POST":
        return render(request, 'app-add-schedules.html')
    elif request.method == "GET":
        return render(request, 'app-add-schedules.html')