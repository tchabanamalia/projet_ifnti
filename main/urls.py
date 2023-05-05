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

    # Abdoul-Malik urls notes
    path('matieres', views.matieres, name='matieres'),
    path('add_notes/<int:id_matiere>', views.createNotesByMatiere, name='add_notes'),
    path('edit_note/<int:id>', views.editeNoteByMatiere, name='edit_note'),
    path('delete_note/<int:id>', views.deleteNote, name='delete_note'),

]