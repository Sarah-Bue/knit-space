# Imports
from django.db import models
from django.contrib.auth.models import User


# The BlogPostAdmin class is adapted from the PostAdmin class
# in Code Institute's "I think therefore I blog" walkthrough
class BlogPost(models.Model):
    """
    Model to represent a blog post within the application.
    """
    # BlogPost fields
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        # Delete all authored posts when user is deleted
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    # Optional excerpt
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('date modified', auto_now=True)

    # String representation of BlogPost showing its title
    def __str__(self):
        return self.title


class SavedPost(models.Model):
    """
    Model to represent a user's saved blog posts.
    """
    # Delete all saved posts from dashboard when user is deleted
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='saved_posts'
    )
    # Delete post from dashboard when post is deleted
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)

    class Meta:
        # Ensure each user can save each post only once
        unique_together = ('user', 'post')

    # String representation indicating which user saved which post
    def __str__(self):
        return f'{self.user.username} saved {self.post.title}'
