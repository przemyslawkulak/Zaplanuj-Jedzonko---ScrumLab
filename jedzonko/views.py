from datetime import datetime

from django.shortcuts import render
from django.views import View

from jedzonko.models import Plan, Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


def main_page(request):
    ctx_plan = Plan.objects.all().count()
    ctx_recipe = Recipe.objects.all().count()
    return render(request, "dashboard.html", {'plans_count': ctx_plan, 'recipe_count': ctx_recipe})
