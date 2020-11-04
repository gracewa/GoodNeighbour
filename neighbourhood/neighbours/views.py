from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood, Business,BlogPost,Profile,Comment
from .forms import ProfileForm,BlogPostForm,BusinessForm,CommentForm, NeighbourhoodForm
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework.response import Response

# Create your views here.

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/update_profile.html', {
        'form': profile_form
    })