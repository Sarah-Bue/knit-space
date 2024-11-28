# Imports
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    View to handle contact form display and submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
            request,
            messages.SUCCESS,
            'Your message has been sent successfully.',
            extra_tags='post_action'
        )

            return redirect('contact')

    else:
        form = ContactForm()
    
    return render(
        request,
        'contact/contact.html',
        {'form': form}
    )
