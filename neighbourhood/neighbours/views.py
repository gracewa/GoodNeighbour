from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood, Business, BlogPost, User, Comment
from .forms import UserForm, BlogPostForm, BusinessForm, CommentForm, NeighbourhoodForm, RegistrationForm, \
    AccountAuthenticationForm, AccountUpdateForm
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q

from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView



def registration_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('hood-list')
        else:
            context = {
                'form': form,
            }

    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('hood-list')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("hood-list")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("hood-list")

    else:
        form = AccountAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, "registration/login.html", context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
                "county": request.POST['county'],
                "estate": request.POST['estate'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )


    blog_posts = BlogPost.objects.filter(username=request.user)
    context = {
        'form': form,
        'blog_posts': blog_posts
    }


    return render(request, "registration/profile.html", context)


class NeighbourhoodListView(ListView):
    model = Neighbourhood

class NeighbourhoodDetailView(DetailView):
    model = Neighbourhood


class UserListView(ListView):
    model = User


class UserCreate(CreateView):
    model = User
    fields = ['name', 'county', 'neighbourhood', 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        location = form.cleaned_data['location']
        county = form.cleaned_data['county']
        return super(UserCreate, self).form_valid(form)


class UserUpdate(UpdateView):
    model = User
    fields = ['name']


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('hood-list')


class NeighbourhoodCreate(CreateView):
    model = Neighbourhood
    fields = ['image','name', 'location', 'admin']


class NeighbourhoodUpdate(UpdateView):
    model = Neighbourhood
    fields = ['name', 'location', 'admin']


class NeighbourhoodDelete(DeleteView):
    model = Neighbourhood
    success_url = reverse_lazy('/')

def hood_detail_view(request,pk):
    hood = Neighbourhood.objects.filter(pk=pk)
    businesses = Business.objects.filter(neighbourhood=pk)
    context = {
        'hood': hood,
        'businesses': businesses
    }

    return render(request, "neighbours/neighbourhood_detail.html", context)

