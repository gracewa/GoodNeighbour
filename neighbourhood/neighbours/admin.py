from django.contrib import admin

# Register your models here.
from .models import Neighbourhood, Business, EmergencyService, Profile


admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(EmergencyService)
admin.site.register(Profile)
