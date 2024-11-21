# Imports
from django.urls import path
from . import views

# URL patterns for Dashboard application

urlpatterns = [
    # URL for deleting posts from dashboard
    
    # URL for user dashboard
    path('', views.user_dashboard, name='user_dashboard'),

    # URL for deleting a post from the dashboard
    path('delete/<int:post_id>/', views.delete_saved_post, name='delete_saved_post'),

    # URL for sorting posts
    path('sort-posts/', views.sort_posts, name='sort_posts'),
]
