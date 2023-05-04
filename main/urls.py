from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    
    # touré-ydaou urls templates latex 30-04-2023
    path('etudiants-l1', views.etudiants_l1, name='etudiants_l1'),
    path('etudiants-l2', views.etudiants_l2, name='etudiants_l2'),
    path('etudiants-l3', views.etudiants_l3, name='etudiants_l3'),
    path('carte-etudiant', views.carte_etudiant, name='carte_etudiant'),
    path('diplome', views.diplome_etudiant, name='diplome_etudiant'),
    path('certificat_scolaire', views.certificat_scolaire, name='certificat_scolaire'),
    path('releve_notes/<str:id>/<str:id_semestre>', views.releve_notes, name='releve_notes'),

    # urls permettant de générer les documents de manière groupée (pour un ensemble d'étudiants)
    path('releve_notes/<str:id_semestre>', views.releve_notes_semestre, name='releve_notes'),



    path('add_note/<int:id_edudiant>/<int:id_matiere>/<int:id_semestre>', views.createNote, name='add-note'),
    path('edit_note/<int:id>', views.editNote, name='edit-note'),
    path('delete_note/<int:id>', views.deleteNote, name='delete-note'),


                               #### Étudiants ####
    path('liste_des_etudiants/', views.etudiants, name='liste_des_etudiants'),
    path('detail_etudiant/<str:id>', views.detailEtudiant, name='detail_etudiant'),
    path('create_etudiant/', views.create_etudiant, name='create_etudiant'),
    path('update_etudiant/<str:id>', views.create_etudiant, name='update_etudiant'),
   
   
                            #### Tuteurs ####
    path('liste_des_tuteurs/', views.tuteurs, name='liste_des_tuteurs'),
    path('detail_tuteur/<int:id>/', views.detailTuteur, name='detail_tuteur'),
    path('create_tuteur/', views.create_tuteur, name='create_tuteur'),
    path('update_tuteur/<int:id>/', views.create_tuteur, name='update_tuteur'),



                            #### Matières ####
    path('liste_des_matieres/', views.matieres, name='liste_des_matieres'),
    path('detail_matiere/<int:id>/', views.detailMatiere, name='detail_matiere'),
    path('create_matiere/', views.create_matiere, name='create_matiere'),
    path('update_matiere/<int:id>/', views.create_matiere, name='update_matiere'),


                            #### UEs ####
    path('liste_des_ues/', views.ues, name='liste_des_ues'),
    path('detail_ue/<int:id>/', views.detailUe, name='detail_ue'),
    path('create_ue/', views.create_ue, name='create_ue'),
    path('update_ue/<int:id>/', views.create_ue, name='update_ue'),



]