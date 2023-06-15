import os
import datetime
from django import forms
from django.http import FileResponse, HttpResponse
from django.shortcuts import render

from django import forms
from main.forms import  EnseignantForm, EtudiantForm, EvaluationForm, InformationForm, NoteForm, TuteurForm, UeForm, MatiereForm

import datetime
from main.pdfMaker import generate_pdf
from .models import Enseignant, Information, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur 
from django.shortcuts import get_object_or_404, redirect, render
from latex import build_pdf
from django.template import loader
from django.conf import settings
from main.forms import  EnseignantForm, EtudiantForm, EvaluationForm, NoteForm, TuteurForm, UeForm, MatiereForm
from .models import Enseignant, Evaluation, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur 
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from main.helpers import *
"""
from main import factory
"""

def index(request):
    return render(request, 'ui.html')


##### Etudiants ####

def etudiants(request): # Retourne toute la liste des étudiants actif
    etudiants = Etudiant.objects.filter(is_active=True)
    context={"etudiants":etudiants}
    return render(request, 'etudiants/etudiants.html', context)


def etudiants_suspendu(request): # Retourne toute la liste des étudiants suspendu
    etudiants = Etudiant.objects.filter(is_active=False)
    context={"etudiants":etudiants}
    return render(request, 'etudiants/etudiants_suspendu.html', context)



def detailEtudiant(request, id): # Retourne le détail d'un etudiant donnée
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
        else:
            print(form.errors)
            return render(request, 'etudiants/create_etudiant.html',{'form':form})



def tuteurs(request): # Retourne toute la liste des tuteurs
    tuteurs=Tuteur.objects.all()
    context={"tuteurs":tuteurs}
    return render(request, 'tuteurs/tuteurs.html', context)



def detailTuteur(request, id): # Retourne le détail d'un tuteur donnée
    tuteur = get_object_or_404(Tuteur, id=id)
    return render(request, "tuteurs/detailTuteur.html", {"tuteur":tuteur})



def create_tuteur(request, id=0): # Création et modification d'un tuteur
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



# Vue pour récupérer la liste des matières par semestre

def matiere_semestre(request, semestre):
    try:
        semestre_obj = Semestre.objects.get(libelle=f'S{semestre}')
        matieres_semestre = Matiere.objects.filter(ue__semestre=semestre_obj)
        template_name = f'matieres/matiere_semestre{semestre}.html'
    except Semestre.DoesNotExist:
        matieres_semestre = []
    context = {
        'matieres_semestre': matieres_semestre
    }
    return render(request, 'matieres/matiere_par_semestre.html', context)



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

# Vue pour récupérer la liste des UE par semestre

def ues_semestre(request, semestre):
    ues = Ue.objects.filter(semestre__libelle=semestre)
    context = {"ues": ues}
    return render(request, 'ues/ues_par_semestre.html', context)








# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L1
def etudiants_l1(request):
    # pour récupérer les étudiants de l1 il faut récupérer les étudiant en S1 et S2
    semestres = Semestre.objects.filter(libelle="S1") | Semestre.objects.filter(libelle="S2") 
    
    etudiants = {'etudiants': [], 'niveau': 'L1', 's1' : semestres[0], 's2' : semestres[1]}
    temp=[]

    # récupération des étudiants de chaque semestres
    for semestre in semestres:
        for etudiant in semestre.etudiant_set.all():
            #ajout de tout les étudiant du semestre dans un tableau temporaire
            temp.append(etudiant)

    # ajout des étudiants dans le dictionnaire
    etudiants['etudiants'] = temp

    return render(request, 'etudiants/list.html', etudiants)






# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L2
def etudiants_l2(request):
    # pour récupérer les étudiants de l1 il faut récupérer les étudiant en S3 et S4
    semestres = Semestre.objects.filter(libelle="S3") | Semestre.objects.filter(libelle="S4") 
    
    etudiants = {'etudiants': [], 'niveau': 'L2', 's1' : semestres[0], 's2' : semestres[1]}
    temp=[]

    # récupération des étudiants de chaque semestres
    for semestre in semestres:
        print(semestre.etudiant_set.all())
        for etudiant in semestre.etudiant_set.all():
            #ajout de tout les étudiant du semestre dans un tableau temporaire
            temp.append(etudiant)

    # ajout des étudiants dans le dictionnaire
    etudiants['etudiants'] = temp

    return render(request, 'etudiants/list.html', etudiants)


# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L3
def etudiants_l3(request):
    # pour récupérer les étudiants de l1 il faut récupérer les étudiant en S1 et S2
    semestres = Semestre.objects.filter(libelle="S5") | Semestre.objects.filter(libelle="S6") 


    
    etudiants = {'etudiants': [], 'niveau': 'L3', 's1' : semestres[0], 's2' : semestres[1]}
    temp=[]

    # récupération des étudiants de chaque semestres
    for semestre in semestres:
        print(semestre.etudiant_set.all())
        for etudiant in semestre.etudiant_set.all():
            #ajout de tout les étudiant du semestre dans un tableau temporaire
            temp.append(etudiant)

    # ajout des étudiants dans le dictionnaire
    etudiants['etudiants'] = temp

    return render(request, 'etudiants/list.html', etudiants)





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
def carte_etudiant(request, id, niveau):
    etudiant = get_object_or_404(Etudiant, id=id)

    print(etudiant.tuteur_set.all())

    context = {'etudiant' : etudiant, 'niveau' : niveau}


    latex_input = 'carte_etudiant'
    latex_ouput = 'generated_carte_etudiant'
    pdf_file = 'pdf_carte_etudiant'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response




#methode générant la carte des étudiants d'un niveau
def carte_etudiant_all(request, niveau):
    

    if niveau == 'L1':
        semestres = Semestre.objects.filter(libelle="S1") | Semestre.objects.filter(libelle="S2") 
        temp=[]

        # récupération des étudiants de chaque semestres
        for semestre in semestres:
            print(semestre.etudiant_set.all())
            for etudiant in semestre.etudiant_set.all():
                #ajout de tout les étudiant du semestre dans un tableau temporaire
                temp.append(etudiant)

        # ajout des étudiants dans le dictionnaire
        context = {'etudiants' : temp, 'niveau' : niveau}


    latex_input = 'carte_etudiant_all'
    latex_ouput = 'generated_carte_etudiant_all'
    pdf_file = 'pdf_carte_etudiant_all'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response






#methode générant le diplome de l'étudiant
def diplome_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    context = {'etudiant' : etudiant}

    latex_input = 'diplome'
    latex_ouput = 'generated_diplome'
    pdf_file = 'pdf_diplome'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response
    
    
#methode générant le diplome de l'étudiant
def diplome_etudiant_all(request):
    semestres = Semestre.objects.filter(libelle="S1") | Semestre.objects.filter(libelle="S2") 
    temp=[]

        # récupération des étudiants de chaque semestres
    for semestre in semestres:
        for etudiant in semestre.etudiant_set.all():
            #ajout de tout les étudiant du semestre dans un tableau temporaire
            temp.append(etudiant)

    # ajout des étudiants dans le dictionnaire
    context = {'etudiants' : temp}

   

    latex_input = 'diplome_all'
    latex_ouput = 'generated_diplome_all'
    pdf_file = 'pdf_diplome_all'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response





#methode générant le certificat scolaire de l'étudiant
def certificat_scolaire(request, id, niveau):
    etudiant = get_object_or_404(Etudiant, id=id)

    context = {'etudiant' : etudiant, 'niveau' : niveau}

    # nom des fichiers d'entrée et de sortie
    # ici pour les test le nom se termine en temp pour signifier temporaire
    # ils seront donc à supprimer
    latex_input = 'template_certificat_scolarite'
    latex_ouput = 'generated_template_certificat_scolarite'
    pdf_file = 'pdf_template_certificat_scolarite'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response






#methode générant le relevé de notes de l'étudiant
def releve_notes(request, id, id_semestre):
    etudiant = get_object_or_404(Etudiant, id=id)
    semestre = get_object_or_404(Semestre, id=id_semestre)

    semestre_ues = get_semester_ues(semestre)

    # récupération et assignation des matières à chacune des UEs
    ues_matieres = get_all_ues_matieres(semestre_ues)


    # récupération et assignation des evaluations au matières des UEs et calcul de la moyenne de l'étudiant dans la matière
    for ue in ues_matieres:
        matieres = ue['matieres']
        # parcours des matières de chaque UEs
        for ue_matieres in matieres:
            matiere = get_object_or_404(Matiere, id=ue_matieres['id'])
            #assignation des evaluations à chaque 
            ue_matieres['evaluations'] = get_all_matiere_evaluations(matiere)
            # calcul des moyennes dans chaque matières
            ue_matieres['moyenne'] = get_matiere_moy(matiere, etudiant)


    # calcul de la moyenne de chaque UE
    for ue in ues_matieres:
        get_ue_moy(ue)
    
    # vérification de la validation des ue par l'étudiant
    for ue in ues_matieres:
        if valid_UE(ue):
            ue['validation'] = 'Validé'
        else:
            ue['validation'] =  'Échec'
        
        


    # #récupération et assignation des notes de chacune des évaluations d'une matière
    # for ue in ues_matieres:
    #     matieres = ue['matieres']
    #     # parcours des matières de chaque UEs
    #     for ue_matieres in matieres:
    #         for evaluation in ue_matieres['evaluations']:
    #             temp_evalution = get_object_or_404(Evaluation, id=evaluation['id'])
    #             evaluation['note'] = get_evaluation_note(temp_evalution,etudiant)


    context = {'etudiant': etudiant, 'semestre' : semestre, 'ues' : ues_matieres}

    # nom des fichiers d'entrée et de sortie

    latex_input = 'releve_notes'
    latex_ouput = 'generated_releve_notes'
    pdf_file = 'pdf_releve_notes'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response
    



#methode générant le relevé de notes des étudiants de tout un semestre
def releve_notes_semestre(request, id_semestre):
    semestre = get_object_or_404(Semestre, id=id_semestre)
    etudiants = semestre.etudiant_set.all()
    context = {'etudiants': etudiants, 'semestre' : semestre}

    # nom des fichiers d'entrée et de sortie

    latex_input = 'releve_notes_semestre'
    latex_ouput = 'generated_releve_notes_semestre'
    pdf_file = 'pdf_releve_notes_semestre'

    #génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response


def evaluations(request, id_matiere):
    """
    Affiche la liste des évaluations d'une matière donnée :model:`main.Matiere`.

    **Context**

    **Template:**

    :template:`main/evaluations/index.html`
    """
    matiere = get_object_or_404(Matiere, pk=id_matiere)
    evaluations = Evaluation.objects.filter(matiere=matiere)
    data = {
        'annee_courrante': '',
        'matiere' : matiere,
        'evaluations' : evaluations,
    }
    
    return render(request, 'evaluations/index.html', data)



def createNotesByEvaluation(request, id_matiere):
    """
    Affiche un formulaire de création d'une évaluation et ensuite d'une note :model:`main.Note` selon la matière.

    **Context**
        'evaluation_form' : formulaire de saisi d'une evaluation,
        'etudiants' : liste des etudiants suivant la matière,
        'notes_formset' : l'ensemble de formulaire,
        'matiere' : matiere,

    **Template:**

    :template:`main/notes/create_or_edit_note.html`
    """    
    matiere = get_object_or_404(Matiere, pk=id_matiere)
    etudiants = matiere.ue.semestre.etudiant_set.all()
    NoteFormSet = forms.modelformset_factory(Note, form=NoteForm, extra=len(etudiants))
    queryset = Note.objects.none()
    
    # Vérifier si le semestre est clôturé
    if not matiere.ue.semestre.semestreCourant:
        messages.error(request, "Le semestre est déjà clôturé. Impossible d'ajouter une évaluation.")
        return redirect('main:evaluations', id_matiere=matiere.id)

    if request.method == 'POST':
        evaluation_form = EvaluationForm(request.POST)
        note_form_set = NoteFormSet(request.POST)
        print(evaluation_form.is_valid())
        print(note_form_set.is_valid())
        if evaluation_form.is_valid() and note_form_set.is_valid():
            evaluation = evaluation_form.save(commit=False)
            evaluation.matiere = matiere
            evaluation.save()
            notes = note_form_set.save(commit=False)
            for note in notes:
                note.evaluation = evaluation
                note.save()
            return redirect('main:evaluations', id_matiere=matiere.id)
    else:
        evaluation_form = EvaluationForm()
        initial_etudiant_note_data = [{'etudiant': etudiant.id, 'etudiant_full_name': etudiant} for etudiant in etudiants]
        note_form_set = NoteFormSet(initial=initial_etudiant_note_data, queryset=queryset)

    data = {
        'evaluation_form': evaluation_form,
        'etudiants': etudiants,
        'notes_formset': note_form_set,
        'matiere': matiere,
        'ponderation_possible': matiere.ponderation_restante(),
    }
    return render(request, 'notes/create_or_edit_note.html', context=data)



def editeNoteByEvaluation(request, id):
    """
    Affiche un formulaire d'édition d'une note :model:`main.Note`.

    **Context**

    ``Note``
        une instance du :model:`main.Note`.

    **Template:**

    :template:`main/notes/create_or_edit_note.html`
    """
    evaluation = get_object_or_404(Evaluation, pk=id)
    matiere = evaluation.matiere
    etudiants = matiere.ue.semestre.etudiant_set.all()
    NoteFormSet = forms.modelformset_factory(Note, form=NoteForm, extra=0)
    queryset=Note.objects.filter(evaluation=evaluation)
    if request.method == 'POST':
        evaluation_form = EvaluationForm(request.POST, instance=evaluation)
        note_form_set = NoteFormSet(request.POST)
        if evaluation_form.is_valid() and note_form_set.is_valid():
            evaluation = evaluation_form.save(commit=False)
            evaluation.matiere = matiere
            evaluation.save()
            notes = note_form_set.save(commit=False)
            for note in notes:
                note.evaluation = evaluation
                note.save()
            return redirect('main:evaluations', id_matiere=matiere.id)
    else :
        evaluation_form = EvaluationForm(instance=evaluation)
        note_form_set = NoteFormSet(queryset=queryset)
        for form in note_form_set:
            form.initial['etudiant_full_name']=Etudiant.objects.filter(id=form.initial['etudiant']).get()
    data = {
        'evaluation_form' : evaluation_form,
        'etudiants' : etudiants,
        'notes_formset' : note_form_set,
        'matiere' : matiere,
        'ponderation_possible' : matiere.ponderation_restante()+evaluation.ponderation,
    }
    return render(request, 'notes/create_or_edit_note.html', context=data)

def deleteEvaluation(request, id):
    """
    Supprime une evaluation :model:`main.Note`.

    **Context**

    ``evaluation``
        une instance du :model:`main.Note`.
    """
    evaluation = get_object_or_404(Evaluation, pk=id)
    matiere = evaluation.matiere
    evaluation.delete()
    return redirect('main:evaluations', id_matiere=matiere.id)


def annee_academique(date):

    annee = date.year
    mois = date.month
    
    if mois < 8:
        annee -= 1
        
    
    return {"annee_academique": f"{annee}-{annee+1}"}


def dashboard(request):
    return render(request, 'dashboard/be_pages_dashboard.html',context=result)


def liste_matieres_professeur(request):
    enseignants_filtrer = Enseignant.objects.exclude(nom="Pas")
    matieres=Matiere.objects.all()

    
    if request.method == "POST":
        enseignant_id = request.POST.get("enseignant")
        enseignant_choisi=Enseignant.objects.get(id=enseignant_id)
        matieres_selectionnees = request.POST.getlist("matieres[]")
        ponderation_choisi=request.POST.getlist("ponderations[]")

        for index, matiere in enumerate(matieres_selectionnees):
            matiere_obj = Matiere.objects.get(libelle=matiere)
            ponderation = float(ponderation_choisi[index])
            matiere_obj.enseignant=enseignant_choisi
            matiere_obj.ponderation =ponderation
            matiere_obj.save()
        
        return render(request, "dashboard/confirmation.html", {"matieres":matieres })
    
    else:
        enseignant_null = Enseignant.objects.get(nom='Pas')
        matieres_filtrer = Matiere.objects.filter(enseignant=enseignant_null)
        context = {'enseignants': enseignants_filtrer, 'matieres': matieres_filtrer}
        return render(request, "dashboard/affectation_prof.html", context)


def retirer_prof(request,pk):
    enseignants_null = Enseignant.objects.get(nom="Pas")
    matiere = Matiere.objects.get(id=pk)
    matiere.enseignant = enseignants_null
    matiere.save()
    return redirect('confirmation_affectation')



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


def enseignant_actif(request):
    enseignants = Enseignant.objects.filter(is_active=True)
    return render(request, 'enseignants/enseignant_list.html', {'enseignants': enseignants})

def enseignant_inactif(request):
    enseignants = Enseignant.objects.filter(is_active=False)
    return render(request, 'enseignants/enseignant_suspendu.html', {'enseignants': enseignants})

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

def certificat_travail(request, id):
    information = get_object_or_404(Information, id=id)
    context = {'information': information}

    # nom des fichiers d'entrée et de sortie
    latex_input = 'certificat_travail'
    latex_ouput = 'generated_certificat_travail'
    pdf_file = 'pdf_certificat_travail'

    # génération du pdf
    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    #visualisation du pdf dans le navigateur
    with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
        pdf_preview = f.read()
        response = HttpResponse(pdf_preview, content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
        return response


def information_list(request):
    informations = Information.objects.all()
    return render(request, 'informations/information_list.html', {'informations': informations})

def information_detail(request, id):
    information = Information.objects.get(id=id)
    return render(request, 'informations/information_detail.html', {'information': information})

def create_information(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = InformationForm()
        else:
            information = Information.objects.get(pk=id)
            form = InformationForm(instance=information)
        return render(request, "informations/create_information.html", {'form': form})
    else:
        if id == 0:
            form = InformationForm(request.POST)
        else:
            information = Information.objects.get(pk=id)
            form = InformationForm(request.POST, instance=information)
        if form.is_valid():
            exit
            form.save()
            return redirect('/main/information_list/')
        else:
            print(form.errors)
            return render(request, "informations/create_information.html", {'form': form})
        
def edit_information(request, id):
    information = Information.objects.get(id=id)
    if request.method == 'POST':
        form = InformationForm(request.POST, request.FILES, instance=information)
        if form.is_valid():
            information = form.save(commit=False)
            information.save()
            return redirect('/main/information_list/')
    else:
        form = InformationForm(instance=information)
    return render(request, 'informations/edit_information.html', {'form': form})


# Cette vue affiche la liste des semestre courants 
def semestres_courants(request):
    semestres=Semestre.objects.filter(semestreCourant = True)
    context={"semestres":semestres}
    return render(request, 'semestres/semestres_courants.html', context)


# Cette vue affiche la liste des semestre clôturés 
def semestres_clotures(request):
    semestres=Semestre.objects.filter(semestreCourant = False)
    context={"semestres":semestres}
    return render(request, 'semestres/semestres_clotures.html', context)


# Cette vue permet de clôturer les semestres 1, 3 et 5 tout en activant automatiquement les semestres 2, 4 et 6
def cloturer_semestre(request, semestre_id):
    semestre = get_object_or_404(Semestre, id=semestre_id)
    semestre.semestreCourant = False
    semestre.save()

    if semestre_id == 'S1-2022-2023':
        semestre_suivant = Semestre.objects.get(id='S2-2022-2023')
        semestre_suivant.semestreCourant = True
        semestre_suivant.save()
    elif semestre_id == 'S3-2022-2023':
        semestre_suivant = Semestre.objects.get(id='S4-2022-2023')
        semestre_suivant.semestreCourant = True
        semestre_suivant.save()
    elif semestre_id == 'S5-2022-2023':
        semestre_suivant = Semestre.objects.get(id='S6-2022-2023')
        semestre_suivant.semestreCourant = True
        semestre_suivant.save()
    else:
        # Si le semestre n'est pas S1, S3 ou S5, rediriger vers une autre page ou afficher un message d'erreur
        return redirect('/main/semestres')
    return redirect('/main/semestres')


# Cette vue permet de réactiver un semestre déjà clôtuté 
def reactiver_semestre(request, semestre_id):
    semestre = get_object_or_404(Semestre, id=semestre_id)
    semestre.semestreCourant = True
    semestre.save()
    return redirect('/main/semestres')



# Cette fonction permet d'afficher la liste des étudiants attché à un semestre 

def historique_semestre(request, semestre_id):
    semestre = Semestre.objects.get(id=semestre_id)
    etudiants = semestre.etudiant_set.all()  # Obtenez tous les étudiants liés à ce semestre
    matieres = Matiere.objects.filter(ue__semestre=semestre)  # Obtenez toutes les matières liées à ce semestre
    evaluations = Evaluation.objects.filter(matiere__ue__semestre=semestre)  # Obtenez toutes les évaluations liées à ce semestre
    notes = Note.objects.filter(evaluation__matiere__ue__semestre=semestre)  # Obtenez toutes les notes liées à ce semestre

    context = {
        'semestre': semestre,
        'etudiants': etudiants,
        'matieres': matieres,
        'evaluations': evaluations,
        'notes': notes,
    }
    
    return render(request, 'semestres/historique_semestre.html', context)



# Cette vue permet d'afficher la liste des étudiants par semestre 
def liste_etudiants_par_semestre(request, semestre):
    semestre_obj = Semestre.objects.get(libelle=semestre)  
    etudiants = semestre_obj.etudiant_set.all()
    context = {
        'etudiants': etudiants
    }
    if etudiants :
        return render(request, 'etudiants/liste_etudiants_par_semestre.html', context)
    return HttpResponse('Pas d\étudiant dans ce semestre')



def passage_etudiants(request):
    if request.method == 'POST':
        etudiant_ids = request.POST.getlist('passer_semestre_suivant')  # Récupère la liste des IDs des étudiants sélectionnés
        
        # Mettre à jour l'attribut passer_semestre_suivant des étudiants sélectionnés
        Etudiant.objects.filter(id__in=etudiant_ids).update(passer_semestre_suivant=True)
        
        # Passer les étudiants au semestre suivant
        semestre_mapping = {
            'S1': 'S2',
            'S2': 'S3',
            'S3': 'S4',
            'S4': 'S5',
            'S5': 'S6',            
        }
        for etudiant_id in etudiant_ids:
            etudiant = Etudiant.objects.get(id=etudiant_id)
            semestres = etudiant.semestre.all()
            
            for semestre in semestres:
                if semestre.libelle in semestre_mapping:
                    semestre_suivant = Semestre.objects.get(libelle=semestre_mapping[semestre.libelle])
                    etudiant.semestre.remove(semestre)
                    etudiant.semestre.add(semestre_suivant)
            
            # Mettre à jour l'attribut passer_semestre_suivant à False
            etudiant.passer_semestre_suivant = False
            etudiant.save()
        
        return redirect('main:passage_etudiants') 
    
    return render(request, 'etudiants/liste_etudiants_par_semestre.html')























