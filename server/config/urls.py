from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from core.views import UserApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/core/', include('core.urls'), name='core'),
    path('api/v1/user', UserApiView.as_view()),
    path('api/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
