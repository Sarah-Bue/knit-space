# Imports
from . import views
from django.urls import path

# URL patterns for Blog application

urlpatterns = [
    # URL for homepage, displaying list of posts
    path('', views.PostList.as_view(), name='home'),

    # URL for individual blog post full-page view, identified by slug
    path('post/<slug:slug>/', views.blogpost_detail, name='blogpost_detail'),

    # URL for saving a blog post by its ID
    path('post/<int:post_id>/save/', views.save_post, name='save_post'),

    # URL for creating new blog posts
    path('create/', views.create_blogpost, name='create_blogpost'),

    # URL for deleting a blog post
    path('delete/<int:post_id>/', views.delete_blogpost, name='delete_blogpost'),

]