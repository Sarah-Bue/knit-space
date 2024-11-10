# Imports

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# The BlogPost model is adapted from the Post model in Code Institute's "I think therefore I blog" walkthrough
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default="deleted user",
        related_name="blog_posts"
    )
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('date modified', auto_now=True)

    def __str__(self):
        return self.title