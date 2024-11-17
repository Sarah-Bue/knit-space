# Imports
from django.db import models
from django.contrib.auth.models import User


# Model to represent a blog post within the application
# The BlogPost model is adapted from the Post model in Code Institute's "I think therefore I blog" walkthrough
class BlogPost(models.Model):
    # BlogPost fields
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        # Fallback to "deleted user" user ID when author-user is deleted
        on_delete=models.SET_DEFAULT,
        default="deleted user",                     # this needs to be changed to user ID of "deleted user"
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


# Model to represent a user's saved blog posts
class SavedPost(models.Model):
    # Delete all saved posts from dashboard when user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_posts')
    # Delete post from dashboard when post is deleted
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)

    class Meta:
        # Ensure each user can save each post only once
        unique_together = ('user', 'post')  

    # String representation indicating which user saved which post
    def __str__(self):
        return f'{self.user.username} saved {self.post.title}'