# Imports
from django.urls import path
from . import views

# Define URL patterns for Dashboard application

urlpatterns = [
    # Dashboard
    path('', views.dashboard_view, name='dashboard'),
]