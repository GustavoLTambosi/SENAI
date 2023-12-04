from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from app_aula.views import home
from app_aula.views import desenvolvedor1
from app_aula.views import desenvolvedor2
from app_aula.views import desenvolvedor3
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('Desenvolvedor1/', desenvolvedor1, name='desenvolvedor1'),
    path('Desenvolvedor2/', desenvolvedor2, name='desenvolvedor2'),
    path('Desenvolvedor3/', desenvolvedor3, name='desenvolvedor3'),
]
