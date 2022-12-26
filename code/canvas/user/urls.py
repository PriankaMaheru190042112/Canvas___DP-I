from django.urls import path
from . import views
from .views import EventDetail
app_name = 'user'


urlpatterns = [
      path('user_auth/',views.registerlogin , name='user_auth'),  
      path('user_home/',views.user_home , name='user_home'),  
      path('user_profile/',views.user_profile , name='user_profile'),  
      path('user_logout/',views.user_logout , name='user_logout'),
      path('eventdetail/<int:pk>/', EventDetail.as_view(),name= 'event_detail'),   
      path('user_gallery/',views.user_gallery , name='user_gallery'), 
      path('user_cart/<int:pk>/', views.user_cart , name='user_cart'),
      path('user_virtual_box/<int:pk>/',views.user_virtual_box , name='user_virtual_box'),
      path('user_join_form/<int:pk>/',views.user_join_form , name='user_join_form')

      
        
]