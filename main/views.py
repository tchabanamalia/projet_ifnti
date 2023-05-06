
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from main.forms import  EnseignantForm, EtudiantForm, TuteurForm, UeForm, MatiereForm
from main.pdfMaker import generate_pdf
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 
from django.shortcuts import get_object_or_404, redirect, render
from main.models_forms import NoteForm




def index(request):
    return render(request, 'ui.html')


 ##### Etudiants ####

def etudiants(request):
    etudiants=Etudiant.objects.all()
    context={"etudiants":etudiants}
    return render(request, 'etudiants/etudiants.html', context)



def detailEtudiant(request, id):
	etudiant = get_object_or_404(Etudiant, id=id)
	return render(request, "etudiants/detailEtudiant.html", {"etudiant":etudiant})


def create_etudiant(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EtudiantForm()
        else:
            etudiant = Etudiant.objects.get(pk=id)
            form = EtudiantForm(instance=etudiant)   
        return render(request, 'etudiants/create_etudiant.html',{'form':form})
    else:
        if id == 0:
            form = EtudiantForm(request.POST)
        else:
            etudiant = Etudiant.objects.get(pk=id)
            form = EtudiantForm(request.POST,instance= etudiant)
        if form.is_valid():
            form.save()
            return redirect('/main/liste_des_etudiants/')








        ##### Tuteurs ####

def tuteurs(request):
    tuteurs=Tuteur.objects.all()
    context={"tuteurs":tuteurs}
    return render(request, 'tuteurs/tuteurs.html', context)



def detailTuteur(request, id):
    tuteur = get_object_or_404(Tuteur, id=id)
    return render(request, "tuteurs/detailTuteur.html", {"tuteur":tuteur})



def create_tuteur(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TuteurForm()
        else:
            tuteur = Tuteur.objects.get(pk=id)
            form = TuteurForm(instance=tuteur)   
        return render(request, 'tuteurs/create_tuteur.html',{'form':form})
    else:
        if id == 0:
            form = TuteurForm(request.POST)
        else:
            tuteur = Tuteur.objects.get(pk=id)
            form = TuteurForm(request.POST,instance= tuteur)
        if form.is_valid():
            form.save()
            return redirect('/main/liste_des_tuteurs/')





        ##### Matières ####

def matieres(request):
    matieres=Matiere.objects.all()
    context={"matieres":matieres}
    return render(request, 'matieres/matieres.html', context)



def detailMatiere(request, id):
	matiere = get_object_or_404(Matiere, id=id)
	return render(request, "matieres/detailMatiere.html", {"matiere":matiere})



def create_matiere(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MatiereForm()
        else:
            matiere = Matiere.objects.get(pk=id)
            form = MatiereForm(instance=matiere)   
        return render(request, 'matieres/create_matiere.html',{'form':form})
    else:
        if id == 0:
            form = MatiereForm(request.POST)
        else:
            matiere = Matiere.objects.get(pk=id)
            form = MatiereForm(request.POST,instance= matiere)
        if form.is_valid():
            form.save()
            return redirect('/main/liste_des_matieres/')



        ##### UEs ####

def ues(request):
    ues=Ue.objects.all()
    context={"ues":ues}
    return render(request, 'ues/ues.html', context)


def detailUe(request, id):
	ue = get_object_or_404(Ue, id=id)
	return render(request, "ues/detailUe.html", {"ue":ue})



def create_ue(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UeForm()
        else:
            ue = Ue.objects.get(pk=id)
            form = UeForm(instance=ue)   
        return render(request, 'ues/create_ue.html',{'form':form})
    else:
        if id == 0:
            form = UeForm(request.POST)
        else:
            ue = Ue.objects.get(pk=id)
            form = UeForm(request.POST,instance= ue)
        if form.is_valid():
            form.save()
            return redirect('/main/liste_des_ues/')








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
        'note_form' : NoteForm(),
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

            ##### Enseignant #####

def create_enseignant(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EnseignantForm()
        else:
            enseignant = Enseignant.objects.get(pk=id)
            form = EnseignantForm(instance=enseignant)
        return render(request, "enseignants/create_enseignant.html", {'form': form})
    else:
        if id == 0:
            form = EnseignantForm(request.POST)
        else:
            enseignant = Enseignant.objects.get(pk=id)
            form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            exit
            form.save()
            return redirect('/main/enseignant_list/')
        else:
            print(form.errors)
            return render(request, "enseignants/create_enseignant.html", {'form': form})


# Read
def enseignant_list(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignants/enseignant_list.html', {'enseignants': enseignants})

def enseignant_detail(request, id):
    enseignant = Enseignant.objects.get(id=id)
    return render(request, 'enseignants/enseignant_detail.html', {'enseignant': enseignant})

# Update
def edit_enseignant(request, id):
    enseignant = Enseignant.objects.get(id=id)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, request.FILES, instance=enseignant)
        if form.is_valid():
            enseignant = form.save(commit=False)
            enseignant.save()
            return redirect('/main/enseignant_list/')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'enseignants/edit_enseignant.html', {'form': form})
