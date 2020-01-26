from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.email
      
