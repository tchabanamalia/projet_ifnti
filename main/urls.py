from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('liste_des_etudiants', views.createEtudiant, name='liste_des_etudiants'),
    
    # touré-ydaou urls templates latex 30-04-2023
    path('etudiants-l1', views.etudiants_l1, name='etudiants_l1'),
    path('etudiants-l2', views.etudiants_l2, name='etudiants_l2'),
    path('etudiants-l3', views.etudiants_l3, name='etudiants_l3'),
    path('carte-etudiant', views.carte_etudiant, name='carte_etudiant'),
    path('diplome', views.diplome_etudiant, name='diplome_etudiant'),
    path('certificat_scolaire', views.certificat_scolaire, name='certificat_scolaire'),
    path('releve_notes', views.releve_notes, name='releve_notes'),

    path('add_note/<int:id_edudiant>/<int:id_matiere>/<int:id_semestre>', views.createNote, name='add-note'),
    path('edit_note/<int:id>', views.editNote, name='edit-note'),
    path('delete_note/<int:id>', views.deleteNote, name='delete-note'),

]