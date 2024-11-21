# Imports
from django import forms
from .models import BlogPost
from django_summernote.widgets import SummernoteWidget

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'excerpt', 'content', 'featured_image']
        widgets = {
            # 'content': forms.Textarea(attrs={'rows': 5}),
            'content': SummernoteWidget()
        }
