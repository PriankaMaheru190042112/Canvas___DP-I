from django.urls import path
from . import views
app_name = 'Admin'


urlpatterns = [
      path('Admin_auth/',views.Admin_auth , name='Admin_auth'),  
      path('Admin_home/',views.Admin_home , name='Admin_home'),  
      path('Admin_profile/',views.Admin_profile , name='Admin_profile'),  
]