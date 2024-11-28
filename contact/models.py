# Imports
from django.db import models


class Contact(models.Model):
    """
    Model for Contact form
    """
    # Fields to store contact information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # Automatic Timestamp
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Messages ordered in descending order of creation date
        ordering = ['-created_on']

    # String representation
    def __str__(self):
        return f"Message from {self.name} - {self.message[:20]}"
