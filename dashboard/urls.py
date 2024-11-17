# Imports
from django.urls import path
from . import views

# Define URL patterns for Dashboard application

urlpatterns = [
    # URL for user dashboard
    path('', views.user_dashboard, name='user_dashboard'),
]