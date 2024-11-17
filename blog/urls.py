# Imports
from . import views
from django.urls import path

# Define URL patterns for Blog application

urlpatterns = [
    # URL for homepage, displaying list of posts
    path('', views.PostList.as_view(), name='home'),
    # URL for saving a blog post by its ID
    path('post/<int:post_id>/save/', views.save_post, name='save_post'),
    # URL for individual blog post full-page view, identified by slug
    path('post/<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),
    # full-page blog post view, redundant?
    # path('<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),
]