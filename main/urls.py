from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('liste_des_etudiants', views.createEtudiant, name='liste_des_etudiants'),
    path('add_note/<int:id_edudiant>/<int:id_matiere>/<int:id_semestre>', views.createNote, name='add-note'),
    path('edit_note/<int:id>', views.editNote, name='edit-note'),
    path('delete_note/<int:id>', views.deleteNote, name='delete-note'),
]