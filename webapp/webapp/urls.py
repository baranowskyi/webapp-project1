from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.urls import urlpatterns as users_urls
from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'), 
      
]

urlpatterns += users_urls
urlpatterns += core_urls
