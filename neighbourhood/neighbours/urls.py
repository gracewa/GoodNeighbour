from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('neighbours.api.urls')),
    path('profile/update/', views.update_profile, name='update_profile'),

]
