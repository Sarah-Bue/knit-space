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
    # Ordered in descending order by created_on
    queryset = BlogPost.objects.all().order_by('-created_on')
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
        messages.add_message(
            request,
            messages.SUCCESS,
            f'"{post.title}" has been saved to your Dashboard.',
            extra_tags='post_action'
        )

    # Redirect to full-page view of saved blog post
    return redirect(
        'blogpost_detail',
        slug=post.slug
    )


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
            return redirect(
                'blogpost_detail',
                slug=blogpost.slug
            )
    else:
        form = BlogPostForm()
    
    # Render in blog/create_blogpost.html template
    return render(
        request,
        'blog/create_blogpost.html',
        {'form': form}
    )


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
    messages.add_message(
        request,
        messages.SUCCESS,
        f'"{blogpost.title}" has been deleted.',
        extra_tags='post_action'
    )

    # Redirect the user to user_blogposts page after deletion
    return redirect(
    'user_blogposts'
    )

    



def edit_blogpost(request, post_id):
    """
    Edit a blog post.
    This is only available after successful login.
    Only post authors can edit their own posts.
    """
    # Retrieve the blog post using post_id
    blogpost = get_object_or_404(BlogPost, id=post_id, author=request.user)
    # Form submission
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS, 
                f'"{blogpost.title}" has been updated.',
                extra_tags='post_action'
            )
            # Redirect to full-page blogpost view after update
            return redirect(
                'blogpost_detail',
                slug=blogpost.slug
            )
    else:
        form = BlogPostForm(instance=blogpost)
    
    # Render in blog/edit_blogpost.html template
    return render(
        request,
        'blog/edit_blogpost.html',
        {'form': form,
        'blogpost': blogpost}
    )


@login_required
def user_blogposts(request):
    """
    Display a list of all blog posts authored by active user.
    This is only available after successful login.
    """
    # Query to retrieve all blog posts authored by active user
    authored_posts = BlogPost.objects.filter(author=request.user)

    # Render in blog/user_blogposts.html template
    return render(
        request,
        'blog/user_blogposts.html',
        {'authored_posts': authored_posts}
    )
