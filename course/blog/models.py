from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import TextInput


class Post(models.Model):

    post_title = models.CharField(max_length=100)
    post_context = models.TextField()
    post_date_posted = models.DateTimeField(default=timezone.now)   
    post_image = models.ImageField()

    def __str__(self):
        return f'{self.post_title}'


class Contact(models.Model):

    STATUS = (
        (1, 'New'),
        (2, 'Read'),
    )

    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'        
    
    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact Form Message"

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
            'name' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad'}),
            'subject' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Mövzu'}),
            'email' : TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ünvanı'}),
            'message' : TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Mesaj'}),  }
