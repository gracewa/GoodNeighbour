from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Business, User, Neighbourhood, EmergencyService, BlogPost, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'username', 'firstname', 'estate', 'county', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'estate', 'county', 'firstname')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['hood']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['username', 'neighbourhood']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']
