# Imports
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin interface for the Contact model.
    """
    list_display = ('name', 'email', 'message', 'created_on')
    search_fields = ('name', 'email')
    ordering = ('-created_on',)
