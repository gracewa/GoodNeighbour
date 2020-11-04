from django.contrib import admin

# Register your models here.
from .models import Neighbourhood, Business, EmergencyService, User
from django.contrib.auth.models import User


admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(EmergencyService)
admin.site.register(User)
