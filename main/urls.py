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
    path('evaluations/<int:id_matiere>', views.evaluations, name='evaluations'),
    path('add_evaluation/<int:id_matiere>', views.createNotesByEvaluation, name='add_evaluation'),
    path('edit_evaluation/<int:id>', views.editeNoteByEvaluation, name='edit_evaluation'),
    path('delete_evaluation/<int:id>', views.deleteEvaluation, name='delete_evaluation'),


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

   

    path('matieres/semestre/1/', views.matiere_semestre, {'semestre': 1}, name='matiere_semestre1'),
    path('matieres/semestre/2/', views.matiere_semestre, {'semestre': 2}, name='matiere_semestre2'),
    path('matieres/semestre/3/', views.matiere_semestre, {'semestre': 3}, name='matiere_semestre3'),
    path('matieres/semestre/4/', views.matiere_semestre, {'semestre': 4}, name='matiere_semestre4'),
    path('matieres/semestre/5/', views.matiere_semestre, {'semestre': 5}, name='matiere_semestre5'),
    path('matieres/semestre/6/', views.matiere_semestre, {'semestre': 6}, name='matiere_semestre6'),




                            #### UEs ####
    path('liste_des_ues/', views.ues, name='liste_des_ues'),
    path('detail_ue/<int:id>/', views.detailUe, name='detail_ue'),
    path('create_ue/', views.create_ue, name='create_ue'),
    path('update_ue/<int:id>/', views.create_ue, name='update_ue'),

                        
                            ### UE par semestre
    path('ues_semestre/semestre1/', views.ues_semestre, {'semestre': 'S1'}, name='ues_semestre1'),
    path('ues_semestre/semestre2/', views.ues_semestre, {'semestre': 'S2'}, name='ues_semestre2'),
    path('ues_semestre/semestre3/', views.ues_semestre, {'semestre': 'S3'}, name='ues_semestre3'),
    path('ues_semestre/semestre4/', views.ues_semestre, {'semestre': 'S4'}, name='ues_semestre4'),
    path('ues_semestre/semestre5/', views.ues_semestre, {'semestre': 'S5'}, name='ues_semestre5'),
    path('ues_semestre/semestre6/', views.ues_semestre, {'semestre': 'S6'}, name='ues_semestre6'),



                            #### Enseignant ####
    path('create_enseignant/', views.create_enseignant, name='create_enseignant'),
    path('enseignant_list/', views.enseignant_list, name='enseignant_list'),
    path('enseignant_detail/(?P<id>[0-9]+)\\Z/', views.enseignant_detail, name='enseignant_detail'),
    path('edit_enseignant/(?P<id>[0-9]+)\\Z/', views.edit_enseignant, name='edit_enseignant'),




## Malia clôture des semestres
    path('semestres/', views.semestres_courants, name='semestres'),
    path('semestres_clotures/', views.semestres_clotures, name='semestres_clotures'),
    path('cloturer_semestre/<str:semestre_id>/', views.cloturer_semestre, name='cloturer_semestre'),
    path('reactiver_semestre/<str:semestre_id>/', views.reactiver_semestre, name='reactiver_semestre'),


## Historique des semestres :
    path('semestre/<str:semestre_id>/historique/', views.historique_semestre, name='historique_semestre'),



### Liste des étudiants par semestres 
    path('liste-etudiants/semestre1/', views.liste_etudiants_par_semestre, {'semestre': 'S1'}, name='liste_etudiants_semestre1'),
    path('liste-etudiants/semestre2/', views.liste_etudiants_par_semestre, {'semestre': 'S2'}, name='liste_etudiants_semestre2'),
    path('liste-etudiants/semestre3/', views.liste_etudiants_par_semestre, {'semestre': 'S3'}, name='liste_etudiants_semestre3'),
    path('liste-etudiants/semestre4/', views.liste_etudiants_par_semestre, {'semestre': 'S4'}, name='liste_etudiants_semestre4'),
    path('liste-etudiants/semestre5/', views.liste_etudiants_par_semestre, {'semestre': 'S5'}, name='liste_etudiants_semestre5'),
    path('liste-etudiants/semestre6/', views.liste_etudiants_par_semestre, {'semestre': 'S6'}, name='liste_etudiants_semestre6'),

    path('passage_etudiants/', views.passage_etudiants, name='passage_etudiants'),












]