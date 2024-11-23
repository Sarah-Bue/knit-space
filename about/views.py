# Imports
from django.shortcuts import render

def about(request):
    """
    Display About page.
    No login required.
    """
    return render(request, 'about/about.html')