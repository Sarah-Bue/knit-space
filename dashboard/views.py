# Standard library imports
import json

# Django imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Local imports
from blog.models import SavedPost


@login_required
def user_dashboard(request):
    """
    Display dashboard for the active user showing their saved blog posts.
    This is only available after successful login.
    """
    # Retrieve all saved posts for active user
    saved_posts = (
        SavedPost.objects.
        filter(user=request.user).order_by('order')
    )
    # Render user's dashboard and pass saved posts to context
    return render(
        request,
        'dashboard/dashboard.html',
        {'saved_posts': saved_posts}
    )


@login_required
def delete_saved_post(request, post_id):
    """
    Delete saved posts and redirect to dashboard.
    This is only available after successful login.
    """
    # Retrieve all saved posts for active user
    saved_post = get_object_or_404(
        SavedPost,
        user=request.user,
        post_id=post_id
    )
    # Delete saved post
    saved_post.delete()
    # Add a success message after deletion

    messages.add_message(
            request,
            messages.SUCCESS,
            f'"{saved_post.post.title}" has been removed from your dashboard.',
            extra_tags='post_action'
        )
    # Redirect back to dashboard
    return redirect('user_dashboard')


@login_required
@csrf_exempt
def sort_posts(request):
    """
    Sort saved posts via AJAX.
    This is only available after successful login.
    The view is temporarily excempt from CSRF verification for AJAX requests
    """
    if request.method == "POST" and request.is_ajax():
        # Retrieve list of post IDs in their order
        order = request.POST.getlist('order[]')
        # If order list is not empty
        if order:
            # Convert order list to a list of integers
            order = list(map(int, order))

            for i, post_id in enumerate(order):
                # Update order field of each saved post
                SavedPost.objects.filter(
                    user=request.user, id=post_id).update(order=i)

            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'})
