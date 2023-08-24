from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from core.views import UserApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/core/', include('core.urls'), name='core'),
    path('index/', UserApiView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
