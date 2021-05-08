from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from moto import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('moto/', include('motocykl.urls')),
    path('', RedirectView.as_view(url='moto/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
