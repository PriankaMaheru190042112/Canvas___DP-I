from django.urls import path
from . import views
app_name = 'Admin'


urlpatterns = [
      path('Admin_auth/',views.Admin_auth , name='Admin_auth'),  
]