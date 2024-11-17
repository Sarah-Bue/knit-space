# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import SavedPost

"""
Display dashboard for the active user showing their saved blog posts.
This is only available after successful login.
"""
@login_required
def user_dashboard(request):
    # Retrieve all saved posts for active user
    saved_posts = SavedPost.objects.filter(user=request.user).select_related('post')
    # Render user's dashboard and pass saved posts to context
    return render(
        request, 
        'dashboard/dashboard.html', 
        {'saved_posts': saved_posts}
    )

"""
Display 
"""
@login_required
def delete_saved_post(request, post_id):
    # Retrieve all saved posts for active user
    saved_post = get_object_or_404(SavedPost, user=request.user, post_id=post_id)
    # Delete saved post
    saved_post.delete()
    # Redirect back to dashboard
    return redirect('user_dashboard')