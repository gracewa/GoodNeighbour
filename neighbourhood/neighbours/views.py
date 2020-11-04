from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood, Business, BlogPost, User, Comment
from .forms import UserForm, BlogPostForm, BusinessForm, CommentForm, NeighbourhoodForm, RegistrationForm
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q

from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def registration_view(request):
    context = {}
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


class NeighbourhoodListView(ListView):
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
    success_url = reverse_lazy('/')


class NeighbourhoodCreate(CreateView):
    model = Neighbourhood
    fields = ['name', 'location', 'admin']


class NeighbourhoodUpdate(UpdateView):
    model = Neighbourhood
    fields = ['name', 'location', 'admin']


class NeighbourhoodDelete(DeleteView):
    model = Neighbourhood
    success_url = reverse_lazy('/')
