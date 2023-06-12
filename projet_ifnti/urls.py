
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('historique/', include('historiques.urls')),
    path('paiement/', include('paiement.urls')),
]
