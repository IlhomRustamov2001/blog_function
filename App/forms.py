from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Blog


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

class BlogForm(forms.ModelForm):
    tags=forms.CharField(max_length=300)
    class Meta:
        model=Blog
        fields=['title', 'content','image','category']