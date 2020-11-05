from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood, Business, BlogPost, User, Comment, EmergencyService
from .forms import UserForm, BlogPostForm, BusinessForm, CommentForm, NeighbourhoodForm, RegistrationForm, \
    AccountAuthenticationForm, AccountUpdateForm, ServiceForm
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


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

@login_required
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

@login_required
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


@staff_member_required
def create_business_view(request, pk):
    form = BusinessForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        hood = Neighbourhood.objects.filter(pk=pk).first()
        obj.neighbourhood = hood
        obj.save()
        form = BusinessForm()

    context = {
        'form':form
    }

    return render(request, "neighbours/business_form.html", context)

class BusinessUpdate(UpdateView):
    model = Business
    fields = ['name', 'description', 'email', 'location', 'phone', 'neighbourhood']

class BusinessDelete(DeleteView):
    model = Business
    success_url = reverse_lazy('hood-list')

class NeighbourhoodCreate(CreateView):
    model = Neighbourhood
    fields = ['image', 'name', 'location', 'admin']

class NeighbourhoodUpdate(UpdateView):
    model = Neighbourhood
    fields = ['image', 'name', 'location', 'admin']


class NeighbourhoodDelete(DeleteView):
    model = Neighbourhood
    success_url = reverse_lazy('hood-list')

@login_required
def hood_detail_view(request, pk):
    hood = Neighbourhood.objects.filter(pk=pk)
    businesses = Business.objects.filter(neighbourhood=pk)
    services = EmergencyService.objects.filter(neighbourhood=pk)
    posts = BlogPost.objects.filter(neighbourhood=pk)
    context = {
        'hood': hood,
        'businesses': businesses,
        'services': services,
        'posts': posts

    }

    return render(request, "neighbours/neighbourhood_detail.html", context)

@staff_member_required
def create_service_view(request, pk):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        hood = Neighbourhood.objects.filter(pk=pk).first()
        obj.neighbourhood = hood
        obj.save()
        form = ServiceForm()

    context = {
        'form':form
    }

    return render(request, "neighbours/service_form.html", context)

class ServiceUpdate(UpdateView):
    model = EmergencyService
    fields = ['type', 'name', 'description', 'location', 'phone']


class ServiceDelete(DeleteView):
    model = EmergencyService
    success_url = reverse_lazy('hood-list')

@login_required
def create_comment_view(request, pk):
    form = CommentForm(request.POST or None, request.FILES or None)
    user = request.user
    if form.is_valid():
        obj = form.save(commit=False)
        blog = BlogPost.objects.filter(pk=pk).first()
        username = User.objects.filter(username=user.username).first()
        obj.post = blog
        obj.username = username
        obj.save()
        form = CommentForm()

    context = {
        'form':form
    }

    return render(request, "neighbours/comment_form.html", context)

@login_required
def create_post_view(request, hood, pk):
    form = BlogPostForm(request.POST or None, request.FILES or None)
    user = request.user
    if form.is_valid():
        obj = form.save(commit=False)
        hood = Neighbourhood.objects.filter(pk=pk).first()
        username = User.objects.filter(username=user.username).first()
        obj.neighbourhood = hood
        obj.username = username
        obj.save()

        form = BlogPostForm()

    context = {
        'form':form,
        'hood': hood
    }

    return render(request, "neighbours/post_form.html", context)