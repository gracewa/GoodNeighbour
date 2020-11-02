from django.urls import path

from .views import NeighbourhoodView


app_name = "api"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('hoods/', NeighbourhoodView.as_view(), name='NeighbourhoodView'),
]
