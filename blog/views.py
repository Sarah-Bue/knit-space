# Imports

from django.shortcuts import render
from django.views import generic
from .models import BlogPost

# Create your views here.

class PostList(generic.ListView):
    # Retrieves all BlogPost objects
    queryset = BlogPost.objects.all()
    # Template used to iterate over all objects for display
    template_name = "blogpost_list.html"
