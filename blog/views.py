# Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import BlogPost, SavedPost


"""
Display all Blog Posts, 9 posts per page.
"""
class PostList(generic.ListView):
    # Retrieves all BlogPost objects, ordered by last_modified un descending order 
    queryset = BlogPost.objects.all().order_by('-last_modified')
    # Template used to render list of blog posts
    template_name = "blog/index.html"
    # Show 9 posts per page
    paginate_by = 9


"""
Display individual Blog Posts.
"""
def blogpost_detail(request, slug):
    # Retrieve all BlogPost objects
    # Return 404 if not found
    queryset = BlogPost.objects.all()
    # Slug identifies BlogPost
    blogpost = get_object_or_404(queryset, slug=slug)

    # Render according to blogpost_detail.html template
    return render(
        request,
        "blog/blogpost_detail.html",
        {"blogpost": blogpost},
    )

"""
Save Blogposts
"""
@login_required
def save_post(request, post_id):
    # Retrieve BlogPost object based on post_id
    # Return 404 if not found
    post = get_object_or_404(BlogPost, id=post_id)
    # Save post to active user's list of saved posts
    SavedPost.objects.get_or_create(user=request.user, post=post)
    # Redirect to full-page view of saved blog post
    return redirect('blogpost_detail', slug=post.slug)