# Imports
from django.db import models

class Contact(models.Model):
    """
    Model for Contact form
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"