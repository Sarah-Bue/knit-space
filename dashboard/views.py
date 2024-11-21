# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import SavedPost
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@login_required
def user_dashboard(request):
    """
    Display dashboard for the active user showing their saved blog posts.
    This is only available after successful login.
    """
    # Retrieve all saved posts for active user
    saved_posts = (
        SavedPost.objects.
        filter(user=request.user)
        .select_related('post')
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
    messages.success(
        request,
        f'"{saved_post.post.title}" has been removed from your dashboard.'
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
                SavedPost.objects.filter(user=request.user, id=post_id).update(order=i)

            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'})
