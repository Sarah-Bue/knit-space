# Imports
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
    A form for creating and updating blog posts.
    WYSIWYG editor for content field.
    """
    class Meta:
        model = BlogPost
        # Define fields
        fields = ['title', 'content', 'excerpt', 'featured_image']
        widgets = {
            'content': SummernoteWidget(),
        }

    def clean_title(self):
        """
        Check for title uniqueness.
        """
        title = self.cleaned_data.get('title')
        if BlogPost.objects.filter(title=title).exists():
            raise forms.ValidationError(
                "A post with this title already exists."
            )
        return title
