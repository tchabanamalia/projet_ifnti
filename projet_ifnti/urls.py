
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('maquette/', include('maquette.urls')),
    path('historique/', include('historiques.urls')),
    path('paiement/', include('paiement.urls')),
] + static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
