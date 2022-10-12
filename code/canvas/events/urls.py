import imp
from re import A
from django.urls import path
from .views import EventDetailView,EventListView

app_name= 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('<int:pk>/', EventDetailView.as_view(),name= 'event-detail'),
    
]
