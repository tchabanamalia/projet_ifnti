from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    
    
    path('dashboard', views.dashboard, name='dashboard'),
    path('prof', views.liste_matieres_professeur, name='liste_matieres_professeur'),
    path('retirer_prof/<int:pk>', views.retirer_prof, name='retirer_prof'),
    

    # touré-ydaou urls templates latex 30-04-2023

    path('etudiants-l1', views.etudiants_l1, name='etudiants_l1'),
    path('etudiants-l2', views.etudiants_l2, name='etudiants_l2'),
    path('etudiants-l3', views.etudiants_l3, name='etudiants_l3'),


    path('carte-etudiant/<str:id>/<str:niveau>', views.carte_etudiant, name='carte_etudiant'),
    path('diplome/<str:id>', views.diplome_etudiant, name='diplome_etudiant'),
    path('certificat_scolaire/<str:id>/<str:niveau>', views.certificat_scolaire, name='certificat_scolaire'),
    path('releve_notes/<str:id>/<str:id_semestre>', views.releve_notes, name='releve_notes'),

    # urls permettant de générer les documents de manière groupée (pour un ensemble d'étudiants)
    path('releve_notes/<str:id_semestre>', views.releve_notes_semestre, name='releve_notes'),
    path('carte-etudiant/<str:niveau>', views.carte_etudiant_all, name='carte_etudiant'),
    path('diplomes', views.diplome_etudiant_all, name='diplome_etudiant'),



    # Abdoul-Malik urls notes
    path('matieres', views.matieres, name='matieres'),
    path('add_notes/<int:id_matiere>', views.createNotesByMatiere, name='add_notes'),
    path('edit_note/<int:id>', views.editeNoteByMatiere, name='edit_note'),
    path('delete_note/<int:id>', views.deleteNote, name='delete_note'),


                               #### Étudiants ####
    path('liste_des_etudiants/', views.etudiants, name='liste_des_etudiants'),
    path('liste_des_etudiants_suspendu/', views.etudiants_suspendu, name='liste_des_etudiants_suspendu'),
    path('detail_etudiant/<str:id>/', views.detailEtudiant, name='detail_etudiant'),    
    path('create_etudiant/', views.create_etudiant, name='create_etudiant'),
    path('update_etudiant/<str:id>/', views.create_etudiant, name='update_etudiant'),   
   
   
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
    path('ues_semestre1/', views.ues_semestre1, name='ues_semestre1'), # Liste des UE du semestre 1
    path('ues_semestre2/', views.ues_semestre2, name='ues_semestre2'), # Liste des UE du semestre 2
    path('ues_semestre3/', views.ues_semestre3, name='ues_semestre3'), # Liste des UE du semestre 3
    path('ues_semestre4/', views.ues_semestre4, name='ues_semestre4'), # Liste des UE du semestre 4
    path('ues_semestre5/', views.ues_semestre5, name='ues_semestre5'), # Liste des UE du semestre 5
    path('ues_semestre6/', views.ues_semestre6, name='ues_semestre6'), # Liste des UE du semestre 6


                            #### Enseignant ####
    path('create_enseignant/', views.create_enseignant, name='create_enseignant'),
    path('enseignant_list/', views.enseignant_list, name='enseignant_list'),
    path('enseignant_detail/(?P<id>[0-9]+)\\Z/', views.enseignant_detail, name='enseignant_detail'),
    path('edit_enseignant/(?P<id>[0-9]+)\\Z/', views.edit_enseignant, name='edit_enseignant'),

]