from django.urls import path
from . import views
from .views import user_auth

app_name = 'user'


urlpatterns = [
      path('user_auth/',views.user_auth , name='user_auth'),  
]