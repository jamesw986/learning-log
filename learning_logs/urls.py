""" Defines URL Patterns for learning_logs """

from django.urls import path

from . import views

app_name = 'learning_logs'
urlspatterns = [
    # Home page
    path('', views.index, name='index'),
]