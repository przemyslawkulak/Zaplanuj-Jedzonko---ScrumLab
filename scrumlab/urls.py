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

from jedzonko.views import IndexView, main_page, recipe_list, carousel, contact_link, about_link, index_link, \
    recipe_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('', carousel, name='landing-page'),
    path('main/', main_page, name="main-page"),
    path('recipe/list/', recipe_list, name="recipe-list"),
    path('contact/', contact_link, name="contact"),
    path('about/', about_link, name="about"),
    path('index/', index_link, name="index"),
    re_path(r'^recipe/(?P<id>(\d)+)', recipe_detail)
]
