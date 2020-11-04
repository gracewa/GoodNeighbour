from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('neighbours.api.urls')),
    path('accounts/register/', views.registration_view, name='register'),

    path('accounts/profile/', views.UserCreate.as_view(), name='user-add'),
    path('profile/<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
    path('profile/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('hoods/add/', views.NeighbourhoodCreate.as_view(), name='hood-add'),
    path('hoods/<int:pk>/', views.NeighbourhoodUpdate.as_view(), name='hood-update'),
    path('hoods/<int:pk>/delete/', views.NeighbourhoodDelete.as_view(), name='hood-delete'),
    path('hoods/', views.NeighbourhoodListView.as_view(), name='hood-list'),
    path('profiles/', views.UserListView.as_view(), name='user-list'),

]
