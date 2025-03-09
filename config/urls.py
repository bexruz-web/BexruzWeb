from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings

from .views import Home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_page, name='Home_page')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)