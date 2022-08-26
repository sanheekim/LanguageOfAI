from django.urls import path, include

from . import views


app_name = 'talkingnotepad' 

urlpatterns = [
    path('', views.index, name='index'),
]