import imp
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
     path('hell/', views.say_hello)
]