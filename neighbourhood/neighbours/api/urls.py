from django.urls import path

from .views import NeighbourhoodView, SingleNeighbourhoodView, SingleUserView, UserView


app_name = "api"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('hoods/', NeighbourhoodView.as_view(), name='NeighbourhoodView'),
    path('hoods/<int:pk>/', SingleNeighbourhoodView.as_view(), name='SingleNeighbourhoodView'),
    path('users/', UserView.as_view(), name='UserView'),
    path('users/<int:pk>/', SingleUserView.as_view(), name='SingleUserView'),
]
