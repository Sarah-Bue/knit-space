# Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import BlogPost, SavedPost
from django.contrib import messages
from .forms import BlogPostForm
from django.utils.text import slugify
from django.urls import reverse
from django.http import HttpResponseRedirect


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


@login_required
def create_blogpost(request):
    """
    Create a new blogpost.
    This is only available after successful login.
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Do not commit the save until after adding the user
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            # Ensure title is not empty and slugify it
            blogpost.slug = slugify(blogpost.title) if blogpost.title else None
            blogpost.save()
            # Redirect to the full-page view of the newly created blog post
            return redirect('blogpost_detail', slug=blogpost.slug)
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_blogpost.html', {'form': form})


def delete_blogpost(request, post_id):
    """
    Delete a blog post.
    This is only available after successful login.
    Only post authors can delete their own posts.
    """
    # Retrieve the blog post using post_id
    blogpost = get_object_or_404(BlogPost, id=post_id, author=request.user)
    # Delete the post
    blogpost.delete()
    # User feedback message
    messages.success(
        request,
        f'"{blogpost.title}" has been deleted.'
    )

    # Redirect the user to their dashboard or home page after deletion
    return HttpResponseRedirect(reverse('home'))
