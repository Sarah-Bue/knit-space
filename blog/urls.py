# Imports

from . import views
from django.urls import path

# Define URL patterns for Blog application

urlpatterns = [
    # home page
    path('', views.PostList.as_view(), name='home'),
    # full-page blog post view
    path('<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),
]