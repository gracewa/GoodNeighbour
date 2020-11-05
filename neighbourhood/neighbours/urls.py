from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('neighbours.api.urls')),
    path('accounts/register/', views.registration_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.account_view, name='profile'),
    path('business/<int:pk>/update', views.BusinessUpdate.as_view(), name='business-update'),
    path('business/<int:pk>/delete/', views.BusinessDelete.as_view(), name='business-delete'),
    path('hoods/<int:pk>/business/add/', views.create_business_view, name='business-add'),
    path('hoods/add/', views.NeighbourhoodCreate.as_view(), name='hood-add'),
    path('hoods/<int:pk>/update/', views.NeighbourhoodUpdate.as_view(), name='hood-update'),
    path('hoods/<int:pk>/delete/', views.NeighbourhoodDelete.as_view(), name='hood-delete'),
    path('', views.NeighbourhoodListView.as_view(), name='hood-list'),
    path('hoods/<int:pk>/', views.hood_detail_view, name='hood-detail'),

    path('profiles/', views.UserListView.as_view(), name='user-list'),
    path('hoods/<int:pk>/service/add/', views.create_service_view, name='service-add'),
    path('service/<int:pk>/update/', views.ServiceUpdate.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', views.ServiceDelete.as_view(), name='service-delete'),
    path('hoods/<int:pk>/post/add/', views.create_post_view, name='post-add'),
    path('hoods/<int:hood>/posts/<int:pk>/comment/add/', views.create_comment_view, name='comment-add'),

]
