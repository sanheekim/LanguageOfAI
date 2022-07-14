from django.urls import URLPattern, path

from . import views

URLPatterns = [
    path('', views.index, name='index'),
    ]