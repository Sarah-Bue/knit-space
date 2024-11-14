# Imports

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BlogPost

# Create your views here.
"""
Display all Blog Posts, 9 posts per page.
"""
class PostList(generic.ListView):
    # Retrieves all BlogPost objects
    queryset = BlogPost.objects.all().order_by('-last_modified')
    # Template used to iterate over all objects for display
    template_name = "blog/index.html"
    # Show 9 posts per page
    paginate_by = 9


"""
Display individual Blog Posts.
"""
def blogpost_detail(request, slug):
    queryset = BlogPost.objects.all()
    blogpost = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/blogpost_detail.html",
        {"blogpost": blogpost},
    )