from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('neighbours.api.urls')),
    path('accounts/register/', views.registration_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.account_view, name='profile'),
    path('profile/<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
    path('profile/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('hoods/add/', views.NeighbourhoodCreate.as_view(), name='hood-add'),
    path('hoods/<int:pk>/update/', views.NeighbourhoodUpdate.as_view(), name='hood-update'),
    path('hoods/<int:pk>/delete/', views.NeighbourhoodDelete.as_view(), name='hood-delete'),
    path('', views.NeighbourhoodListView.as_view(), name='hood-list'),
    path('hoods/<int:pk>/', views.hood_detail_view, name='hood-detail'),

    path('profiles/', views.UserListView.as_view(), name='user-list'),

]
