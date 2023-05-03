from django.shortcuts import get_object_or_404, redirect, render

from main.models_forms import NoteForm
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 


def index(request):
    return render(request, 'ui.html')

def createEtudiant(request):
    etudiants=Etudiant.objects.all()
    context={"etudiants":etudiants}
    return render(request, 'etudiants/create.html', context)



def createNote(request, id_etudiant, id_matiere, id_semestre):
    """
    Affiche un formulaire de création d'une note :model:`main.Note`.

    **Context**

    ``Note``
        une instance du :model:`main.Note`.

    **Template:**

    :template:`main/notes/create_or_edit_note.html`
    """
    data = {
        'note_form' : NoteForm(),
        'etudiant' : get_object_or_404(Etudiant, pk=id_etudiant),
        'matiere' : get_object_or_404(Matiere, pk=id_matiere),
        'semestre' : get_object_or_404(Semestre, pk=id_semestre),
    }
    if request.method == 'POST':
        noteForm = NoteForm(request.POST)
        if noteForm.is_valid():
            noteForm.save()
            return redirect('main:index')
        data['note_form'] = noteForm
    return render(request, 'notes/create_or_edit_note.html', context=data)

def editNote(request, id):
    """
    Affiche un formulaire d'édition d'une note :model:`main.Note`.

    **Context**

    ``Note``
        une instance du :model:`main.Note`.

    **Template:**

    :template:`main/notes/create_or_edit_note.html`
    """
    note = get_object_or_404(Note, pk=id)
    data = {
        'note_form' : NoteForm(request.POST, instance=Note),
        'etudiant' : note.etudiant,
        'matiere' :  note.matiere,
        'semestre' : note.semestre,
    }
    if request.method == 'POST':
        noteForm = NoteForm(request.POST)
        if noteForm.is_valid():
            noteForm.save()
            return redirect('main:index')
        data['note_form'] = noteForm
    return render(request, 'notes/create_or_edit_note.html', context=data)

def deleteNote(request, id):
    """
    Supprime une note :model:`main.Note`.

    **Context**

    ``Note``
        une instance du :model:`main.Note`.
    """
    note = get_object_or_404(Note, pk=id)
    note.delete()
    return redirect('main:index')