from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_auth/', views.user_auth, name='user_auth'),
    path('organization_auth/', views.organization_auth, name='organization_auth'),
    
]