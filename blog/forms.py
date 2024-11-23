# Imports
from django import forms
from .models import BlogPost
from django_summernote.widgets import SummernoteWidget

class BlogPostForm(forms.ModelForm):
    """
    A form for creating and updating blog posts.
    CSS classes used to enhance styling and responsiveness.
    """
    class Meta:
        model = BlogPost
        # Define fields
        fields = ['title', 'excerpt', 'content', 'featured_image']
        widgets = {
            # Set CSS classes to enable styling
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        }
