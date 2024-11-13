from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.user.urls')),
    path('report/', include('core.report.urls')),
    path('messaging/', include('core.messaging.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)