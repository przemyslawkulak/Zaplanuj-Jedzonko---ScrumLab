"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from jedzonko.views import main_page, recipe_list, contact_link, about_link, index_link, plan_list, recipe_add, \
    recipe_detail, new_plan, recipe_modify, plan_details, add_plan_detail, app_login, registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_link, name='landing-page'),
    path('login/', app_login, name='login-page'),
    path('registration/', registration, name="register-page"),
    path('main/', main_page, name="main-page"),
    path('recipe/list/', recipe_list, name="recipe-list"),
    path('recipe/add/', recipe_add, name="new-recipe"),
    path('contact/', contact_link, name="contact"),
    path('about/', about_link, name="about"),
    path('plan/add/', new_plan, name="new-plan"),
    re_path(r'^recipe/modify/(?P<id>(\d)+)/', recipe_modify),
    re_path(r'^plan/(?P<id>(\d)+)/', plan_details),
    re_path(r'^recipe/(?P<id>(\d)+)', recipe_detail, name="recipe-detail-view"),
    path('plan/list/', plan_list, name="plan-list"),
    path('plan/add/details/', add_plan_detail, name="add-plan-detail"),
]
