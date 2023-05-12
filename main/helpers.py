from django.shortcuts import get_object_or_404
from main.models import Etudiant, Note, Ue



# MAIN HELPER FUNCTIONS

"""
    Ce fichier correspond à des fonctions (d'aide) pouvant être appelés 
    à n'importe quel endroit de l'application. Dans ce fichier seront 
    donc définies toutes les fonctions qui serviront au développement
"""






# fonction permettant de retourner toutes les UEs d'un semestre

"""
    paramètre(s) : Semestre semestre
    retour : tableau dictionnaire d'UEs 

"""
def get_semester_ues(semestre):
    semestre_ues = Ue.objects.filter(semestre__libelle = semestre.libelle)

    # création du tableau d'UEs
    ues_list = []
    for ue in semestre_ues:
        ues_list.append({ 'id': ue.id, 'libelle' : ue.libelle, 'nbreCredits' : ue.nbreCredits, 'heures' : ue.heures, 'enseignant' : ue.enseignant, 'semestre': ue.semestre})
    
    return ues_list





# cette fonction retourne de manière formatée l'ensemble des matières d'un ensemble d'UEs

"""
    paramètre(s) : tableau de dictionnaire d'UEs
    retour : tableau de dictionnaire d'UE avec une valeur en plus tableau de dictionnaire de matière
"""
def get_all_ues_matieres(ues_list):
    # ici nous parcourons l'ensemble de nos ue pour récupérer leur ensemble de matières
    for ue in ues_list:
        # nous récupérons l'objet UE en base afin de récupérer les matières
        get_ue = get_object_or_404(Ue, id=ue['id'])
        #création du tableau de dictionnaire de matières
        ue_matieres = get_ue.matiere_set.all()
        # création du tableau de matières de l'UE
        tab_matiere_temp = []
        for matiere in ue_matieres:
            # création des dictionnaires temporaires
            dict_matiere_temp = {'id' : matiere.id, 'codematiere' : matiere.codematiere, 'libelle' : matiere.libelle, 'coefficient' : matiere.coefficient, 'minValue' : matiere.minValue, 'enseignant' : matiere.enseignant, 'is_active' : matiere.is_active}
            # ajout des dictionnaires au tableau de matières de l'UE
            tab_matiere_temp.append(dict_matiere_temp)
        # ajout du tableau de matière de l'UE au dictionnaire de l'UE
        ue['matieres'] = tab_matiere_temp
    return ues_list






# cette fonction retourne sous la forme d'un tableau de dictionnaire les evaluations d'une matière

"""
    paramètre(s) : Matiere matiere
    retour : tableau d'évaluations

"""

def get_all_matiere_evaluations(matiere):
    evaluations = matiere.evaluation_set.all()
    evaluations_tab = []
    for evaluation in evaluations:
        # création d'un dictionnaire temporaire et ajout de celui-ci au tableau d'évaluations
        temp_dict_evalution = {'id' : evaluation.id, 'libelle' : evaluation.libelle, 'date' : evaluation.date}
        evaluations_tab.append(temp_dict_evalution)
    return evaluations_tab





# cette fonction retourne l'ensemble des notes d'une évaluation

"""
    paramètre(s) : Evaluation evaluation
    retour : tableau de notes
"""

def get_evaluation_note(evaluation, etudiant):
    note = Note.objects.filter(etudiant=etudiant, evaluation=evaluation)
    if note:
        return note[0].valeurNote
    return 0

