import imp
from re import A
from django.urls import path
from .views import EventsView,EventDetail
from . import views

app_name= 'organization'

urlpatterns = [
      
      path('organization_auth/',views.registerlogin , name='organization_auth'),
      path('organization_home/',views.organization_home, name='organization_home'),
      path('organization_logout/',views.organization_logout, name='organization_logout'),
      path('organization_profile/',views.organization_profile, name='organization_profile'),
      path('eventform/',views.eventform , name='eventform'),
      # path('eventlist/', EventsView.as_view(), name='event_list'),
      path('eventdetail/<int:pk>/', EventDetail.as_view(),name= 'event_detail'),   
]
