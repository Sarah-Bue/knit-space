# Imports
from django.urls import path
from . import views

# Define URL patterns for Dashboard application

urlpatterns = [
    # URL for deleting posts from dashboard
    path('delete/<int:post_id>/', views.delete_saved_post, name='delete_saved_post'),
    # URL for user dashboard
    path('', views.user_dashboard, name='user_dashboard'),
]