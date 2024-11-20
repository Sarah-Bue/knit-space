# Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import BlogPost, SavedPost
from django.contrib import messages


class PostList(generic.ListView):
    """
    Display all Blog Post previews, 9 posts per page.
    No login required.
    """
    # Retrieves all BlogPost objects
    # Ordered in descending order by last_modified
    queryset = BlogPost.objects.all().order_by('-last_modified')
    # Template used to render list of blog posts
    template_name = "blog/index.html"
    # Show 9 posts per page
    paginate_by = 9


def blogpost_detail(request, slug):
    """
    Display individual Blog Posts.
    No login required.
    """
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


@login_required
def save_post(request, post_id):
    """
    Save Blogposts to dashboard.
    This is only available after successful login.
    """
    # Retrieve BlogPost object based on post_id
    # Return 404 if not found
    post = get_object_or_404(BlogPost, id=post_id)
    # Save post to active user's list of saved posts
    saved, created = SavedPost.objects.get_or_create(
        user=request.user,
        post=post
    )

    # If post was saved / created, add a success message
    if created:
        messages.success(
            request,
            f'"{post.title}" has been saved to your Dashboard.'
        )

    # Redirect to full-page view of saved blog post
    return redirect('blogpost_detail', slug=post.slug)
