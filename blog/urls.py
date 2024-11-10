from . import views
from django.urls import path

# Define URL patterns for Blog application

urlpatterns = [
    # home page
    path('', views.PostList.as_view(), name='home'),
]