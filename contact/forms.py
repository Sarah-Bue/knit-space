# Imports
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for contact submissions
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
