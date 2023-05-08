
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from django import forms
from main.forms import  EnseignantForm, EtudiantForm, EvaluationForm, NoteForm, TuteurForm, UeForm, MatiereForm

import datetime
from main.pdfMaker import generate_pdf
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 
from django.shortcuts import get_object_or_404, redirect, render



def index(request):
    return render(request, 'ui.html')


 ##### Etudiants ####

def etudiants(request): # Retourne toute la liste des étudiants actif
    #etudiants=Etudiant.objects.all()
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










        ##### Tuteurs ####

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


def matieres_semestre_1(request):
    # Récupération du semestre 1
    semestre_1 = get_object_or_404(Semestre, libelle='S1')
    matieres = Matiere.objects.filter(ue__semestre=semestre_1)
    context = {'matieres': matieres}
    return render(request, 'matieres/matiere_semestre1.html', context)



def matieres_semestre_2(request):
    semestre_2 = get_object_or_404(Semestre, libelle='S2')
    matieres = Matiere.objects.filter(ue__semestre=semestre_2)
    context = {'matieres': matieres}
    return render(request, 'matieres/matiere_semestre2.html', context)



def matieres_semestre_3(request):
    # Récupération du semestre 3
    semestre_3 = get_object_or_404(Semestre, libelle='S3')
    matieres = Matiere.objects.filter(ue__semestre=semestre_3)
    context = {'matieres': matieres}
    return render(request, 'matieres/matiere_semestre3.html', context)



def matieres_semestre_4(request):
    # Récupération du semestre 4
    semestre_4 = get_object_or_404(Semestre, libelle='S3')
    matieres = Matiere.objects.filter(ue__semestre=semestre_4)
    context = {'matieres': matieres}
    return render(request, 'matieres/matiere_semestre4.html', context)



def matieres_semestre_5(request):
    # Récupération du semestre 5
    semestre_5 = get_object_or_404(Semestre, libelle='S3')
    matieres = Matiere.objects.filter(ue__semestre=semestre_5)
    context = {'matieres': matieres}
    return render(request, 'matieres/matiere_semestre5.html', context)



def matieres_semestre_6(request):
    # Récupération du semestre 1
    semestre_6 = get_object_or_404(Semestre, libelle='S3')
    matieres = Matiere.objects.filter(ue__semestre=semestre_6)
    context = {'matieres': matieres}
    return render(request, 'matieres/matiere_semestre6.html', context)






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

# Vue pour récupérer la liste des UEs par semestre

def ues_semestre1(request):
    ues = Ue.objects.filter(semestre__libelle='S1')
    context = {"ues": ues}
    return render(request, 'ues/ues_semestre1.html', context)


def ues_semestre2(request):
    ues = Ue.objects.filter(semestre__libelle='S2')
    context = {"ues": ues}
    return render(request, 'ues/ues_semestre2.html', context)


def ues_semestre3(request):
    ues = Ue.objects.filter(semestre__libelle='S3')
    context = {"ues": ues}
    return render(request, 'ues/ues_semestre3.html', context)


def ues_semestre4(request):
    ues = Ue.objects.filter(semestre__libelle='S4')
    context = {"ues": ues}
    return render(request, 'ues/ues_semestre4.html', context)


def ues_semestre5(request):
    ues = Ue.objects.filter(semestre__libelle='S5')
    context = {"ues": ues}
    return render(request, 'ues/ues_semestre5.html', context)


def ues_semestre6(request):
    ues = Ue.objects.filter(semestre__libelle='S6')
    context = {"ues": ues}
    return render(request, 'ues/ues_semestre6.html', context)



# Vue pour récupérer la liste des matières par semestre
def matieres_par_semestre(request):
    semestres = Semestre.objects.all()
    matieres_par_semestre = {}

    # Parcours de chaque semestre
    for semestre in semestres:
        # Récupération des matières pour ce semestre
        matieres = Matiere.objects.filter(ue__semestre=semestre)
        matieres_par_semestre[semestre.libelle] = matieres
    context = {'matieres_par_semestre': matieres_par_semestre}
    return render(request, 'matieres/matieres_semestre1.html', context)







# methode qui normalement doit retourner sur le template affichant l'ensemble des élèves de L1
def etudiants_l1(request):
    # pour récupérer les étudiants de l1 il faut récupérer les étudiant en S1 et S2
    semestres = Semestre.objects.filter(libelle="S1") | Semestre.objects.filter(libelle="S2") 
    
    etudiants = {'etudiants': [], 'niveau': 'L1', 's1' : semestres[0], 's2' : semestres[1]}
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
def releve_notes(request, id, id_semestre):
    etudiant = get_object_or_404(Etudiant, id=id)
    semestre = get_object_or_404(Semestre, id=id_semestre)
    context = {'etudiant': etudiant, 'semestre' : semestre}

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


def matieres(request):
    """
    Affiche la liste des matiers de l'année et du semestre actuelle :model:`main.Matiere`.

    **Context**

    **Template:**

    :template:`main/matieres/index.html`
    """
    # Déterminer l'année courrante
    annee_academique = AnneeUniversitaire.objects.filter(anneeUnivCourrante=True)
    # Détérminier les semestres courrants : il sont toujours trois : s1, s3, s5 ou s2, s4, s6
    # Rechercher les Ues selon les semèstre
    # Rechercher la liste des matières pour chaque Ue
    #  
    data = {
        'annee_courrante': '',
        'semestres_courrant': [],
        'annees_semestres_matieres' : [],
    }
    
    return render(request, 'matieres/index.html', data)

def createNotesByMatiere(request, id_matiere):
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
    if request.method == 'POST':
        evaluation_form = EvaluationForm(request.POST)
        note_form_set = NoteFormSet(request.POST)
        if evaluation_form.is_valid() and note_form_set.is_valid():
            evaluation = evaluation_form.save(commit=False)
            evaluation.matiere = matiere
            evaluation.save()
            notes = note_form_set.save(commit=False)
            for note in notes:
                note.evaluation = evaluation
                note.save()
            return redirect('success')
    else :
        evaluation_form = EvaluationForm()
        initial_etudiant_note_data = [{'etudiant' : etudiant.id, 'etudiant_full_name': etudiant} for etudiant in etudiants]
        note_form_set = NoteFormSet(initial=initial_etudiant_note_data)
    
    data = {
        'evaluation_form' : evaluation_form,
        'etudiants' : etudiants,
        'notes_formset' : note_form_set,
        'matiere' : matiere,
    }
    return render(request, 'notes/create_or_edit_note.html', context=data)

def editeNoteByMatiere(request, id):
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


def annee_academique(date):

    annee = date.year
    mois = date.month
    
    if mois < 8:
        annee -= 1
        
    
    return {"annee_academique": f"{annee}-{annee+1}"}

date = datetime.date.today()
result = annee_academique(date)
annee_univ = AnneeUniversitaire(anneeUniv=result["annee_academique"])
annee_univ.save()

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

