# Imports
from django.shortcuts import render
from .models import About


def about(request):
    """
    Display About page.
    No login required.
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
