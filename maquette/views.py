from django.http import HttpResponse
from django.shortcuts import render
from main.pdfMaker import generate_pdf
from main.models import AnneeUniversitaire, Programme, Semestre, Ue, Domaine, Parcours

def generate_maquette(request):
    if request.method == "POST":
        domaine = Domaine.objects.all()[0]
        parcours = Parcours.objects.filter(domaine=domaine)[0]
        annee_accademique = AnneeUniversitaire.objects.filter(anneeUniv="2023-03-18")[0]
        semestre = Semestre.objects.all()[0]
        #print(semestre)
        programmes = Programme.objects.filter(semestre=semestre, parcours=parcours, anneescolaire=annee_accademique)
        #print(programmes)
        ues = [programme.ue for programme in programmes]
        #print(ues)
        ues_list = []
        for ue in ues:
            matires = [matiere.libelle for matiere in ue.matiere_set.all()]
            horaires = [matiere.heures for matiere in ue.matiere_set.all()]
            enseignants = [matiere.enseignant.__str__() for matiere in ue.matiere_set.all()]
            enseignant_principale = [ue.enseignant for _ in enseignants]
            ue_dict = {
                    "intitule" : ue.libelle,
                    "type_ue" : ue.type,
                    "matieres" : matires,
                    "credit" : ue.nbreCredits,
                    "volumes_horaires" : horaires,
                    "enseignants" : enseignants,
                    "enseignants_principaux" : enseignant_principale,
                }
            ues_list.append(ue_dict)
        
        #print(ues_list[0]['matieres'])
        data={
            "semestre" : semestre.libelle,
            "tatale_credit" : sum([ue["credit"] for ue in ues_list]),
            "totale_volume_horaire" : sum(horaires),
            "ues" : ues_list
        }
        generate_maquette_pdf(data)
    data = {
        "semestres" : Semestre.objects.all(),
        "domaines" : Domaine.objects.all(),
        "parcours" : Parcours.objects.all(),
        "type_maquettes" : ["Spécifique", "Générique"],
    }
    return render(request, "maquette/generate_maquette.html", data)

def generate_maquette_pdf(context):

    latex_input = 'maquette_generique_template'
    latex_ouput = 'maquette_generique'
    pdf_file = 'maquette/maquette_generique'

    generate_pdf(context, latex_input, latex_ouput, pdf_file)

    # with open('media/pdf/' + str(pdf_file) + '.pdf', 'rb') as f:
    #     pdf_preview = f.read()
    #     response = HttpResponse(pdf_preview, content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline;filename=pdf_file.pdf'
    #     return response
    