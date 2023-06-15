from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.generate_maquette, name=''),
    path('', views.generate_maquette_pdf, name=''),
]