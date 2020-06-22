from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('trabajos/', views.trabajos, name="trabajos"),
    path('trabajos/<slug:slug_text>', views.detalles),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
