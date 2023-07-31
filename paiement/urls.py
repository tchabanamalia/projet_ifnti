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
    
                            #### Fiche de Paie ####
                            
    # URL pour lister toutes les fiches de paie
    path('fiche_de_paie_list/', views.fiche_de_paie_list, name='fiche_de_paie_list'),

    # URL pour afficher les détails d'une fiche de paie
    path('fiche_de_paie_detail/<int:id>/', views.fiche_de_paie_detail, name='fiche_de_paie_detail'),

    # URL pour créer une nouvelle fiche de paie
    path('create_fiche_de_paie/', views.create_fiche_de_paie, name='create_fiche_de_paie'),

    # URL pour mettre à jour une fiche de paie existante
    path('update_fiche_de_paie/<int:id>/', views.update_fiche_de_paie, name='update_fiche_de_paie'),
    
     # URL pour générer le fichier PDF de la fiche de paie
    path('fiche_paie/<int:id>/', views.fiche_paie, name='fiche_paie'),
    
    

]