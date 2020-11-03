from django import forms
from .models import Business, Profile, Neighbourhood, EmergencyService, BlogPost, Comment


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['admin']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user', 'neighbourhood']

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

