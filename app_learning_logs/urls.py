"""Defines URL patterns for app_learning_logs."""
from django.urls import path

from . import views

app_name = "app_learning_logs"
urlpatterns = [
    # Home Page
    path("", views.index, name="index")
]
