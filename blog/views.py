# Imports

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPost

# Create your views here.

class PostList(generic.ListView):
    # Retrieves all BlogPost objects
    queryset = BlogPost.objects.all()
    # Template used to iterate over all objects for display
    template_name = "blog/index.html"
    paginate_by = 9


"""
Display individual Blog Post
"""
def post_detail(request, slug):
    queryset = BlogPost.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )