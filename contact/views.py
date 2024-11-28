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
            # Save Form
            form.save()
            # Success Feedback Message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your message has been sent successfully.',
                extra_tags='post_action'
            )

            # Return to Contact Page
            return redirect('contact')

    # Emtpy form if request is not POST
    else:
        form = ContactForm()

    # Render view in contact.html template
    return render(
        request,
        'contact/contact.html',
        {'form': form}
    )
