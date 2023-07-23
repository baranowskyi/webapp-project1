from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.urls import urlpatterns as users_urls
from core.urls import urlpatterns as core_urls
from core.api.urls import urlpatterns as api_core_urls

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('control/admin/', admin.site.urls), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += users_urls
urlpatterns += api_core_urls
urlpatterns += core_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    