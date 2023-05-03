
from django.http import HttpResponse
from django.shortcuts import render

from main.pdfMaker import generate_pdf
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 

from django.shortcuts import get_object_or_404, redirect, render


from main.models_forms import NoteForm
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 


def index(request):
    return render(request, 'ui.html')

def createEtudiant(request):
    etudiants=Etudiant.objects.all()
    context={"etudiants":etudiants}
    return render(request, 'etudiants/create.html', context)

# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L1
def etudiants_l1(request):
    return render(request, 'etudiants/list.html')

# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L2
def etudiants_l2(request):
    return render(request, 'etudiants/list.html')


# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L3
def etudiants_l3(request):
    return render(request, 'etudiants/list.html')





"""
    Pour la génération des documents pdf, la méthode generate_pdf 
    permet de générer tout type de document et prend en paramètre:
        * le contexte
        * le nom du fichier latex servant de template
        * le nom du fichier latex qui sera généré en sortie
        * le nom du fichier pdf qui sera généré en sortie
        ( pour les fichier ne pas mentionner l'extension )
"""

#methode générant la carte de l'étudiant
def carte_etudiant(request):
    context = {}

    # nom des fichiers d'entrée et de sortie
    # ici pour les test le nom se termine en temp pour signifier temporaire
    # ils seront donc à supprimer
    latex_input = 'carte_etudiant_temp'
    latex_ouput = 'generated_carte_etudiant_temp'
    pdf_file = 'pdf_carte_etudiant_temp'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response
    

#methode générant le diplome de l'étudiant
def diplome_etudiant(request):
    context = {}

    # nom des fichiers d'entrée et de sortie
    # ici pour les test le nom se termine en temp pour signifier temporaire
    # ils seront donc à supprimer
    latex_input = 'diplome_temp'
    latex_ouput = 'generated_diplome_temp'
    pdf_file = 'pdf_diplome_temp'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response
    

#methode générant le certificat scolaire de l'étudiant
def certificat_scolaire(request):
    context = {}

    # nom des fichiers d'entrée et de sortie
    # ici pour les test le nom se termine en temp pour signifier temporaire
    # ils seront donc à supprimer
    latex_input = 'template_certificat_scolarite_temp'
    latex_ouput = 'generated_template_certificat_scolarite_temp'
    pdf_file = 'pdf_template_certificat_scolarite_temp'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response
    


#methode générant le relevé de notes de l'étudiant
def releve_notes(request):
    context = {}

    # nom des fichiers d'entrée et de sortie
    # ici pour les test le nom se termine en temp pour signifier temporaire
    # ils seront donc à supprimer
    latex_input = 'releve_notes_temp'
    latex_ouput = 'generated_releve_notes_temp'
    pdf_file = 'pdf_releve_notes_temp'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response



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

