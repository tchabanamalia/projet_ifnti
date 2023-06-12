from django.urls import path
from . import views

app_name = 'paiement'

urlpatterns = [

                            #### Comptable ####
    path('create_comptable/', views.create_comptable, name='create_comptable'),
    path('comptable_detail/(?P<id>[0-9]+)\\Z/', views.comptable_detail, name='comptable_detail'),
    path('edit_comptable/(?P<id>[0-9]+)\\Z/', views.edit_comptable, name='edit_comptable'),
    path('comptable_list/', views.comptable_list, name='comptable_list'),


                            #### Paiement ####
    path('paiement_list/', views.paiement_list, name='paiement_list'),
    path('paiement_detail/(?P<id>[0-9]+)\\Z/', views.paiement_detail, name='paiement_detail'),
    path('create_paiement/', views.create_paiement, name='create_paiement'),
    path('edit_paiement/(?P<id>[0-9]+)\\Z/', views.edit_paiement, name='edit_paiement'),

]