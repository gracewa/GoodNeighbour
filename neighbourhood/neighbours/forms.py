from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Business, User, Neighbourhood, EmergencyService, BlogPost, Comment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'username', 'firstname', 'estate', 'county', 'password1', 'password2', )


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['admin']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        exclude=['hood']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        exclude=['username','neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']

