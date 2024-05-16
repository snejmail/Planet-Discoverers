from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Planet_Discoverers.common.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Planet_Discoverers.common.urls')),
    path('users/', include('Planet_Discoverers.users.urls')),
    path('planets/', include('Planet_Discoverers.planets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = custom_404_view
