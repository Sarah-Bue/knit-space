# Imports
from . import views
from django.urls import path

# URL patterns for Contact application

urlpatterns = [
    path('', views.contact, name='contact'),
]