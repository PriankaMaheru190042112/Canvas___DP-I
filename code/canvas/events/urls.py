import imp
from re import A
from django.urls import path
from .views import EventDetailView,EventListView
from django.conf import settings
from django.conf.urls.static import static

app_name= 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('<int:pk>/', EventDetailView.as_view(),name= 'event-detail'),
    
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
