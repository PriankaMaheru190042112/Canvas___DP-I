from asyncio import events
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls', namespace='events')),
    path('organization/', include('organization.urls', namespace='organization')),
    path('user/', include('user.urls', namespace='user')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)