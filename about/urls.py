# Imports
from django.urls import path
from . import views

# URL patterns for About application

urlpatterns = [
    path('', views.about, name='about'),
]
