# Imports
from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for About section
    """

    summernote_fields = ('content',)