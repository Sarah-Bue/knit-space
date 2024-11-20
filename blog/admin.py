# Imports
from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


# The BlogPostAdmin class is adapted from the PostAdmin class
# in Code Institute's "I think therefore I blog" walkthrough
@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    """
    Customized Django Admin interface.
    Includes Summernote as WYSIWYG text editing.
    """
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
