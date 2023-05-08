from django.contrib import admin
from .models import Enseignant, Evaluation, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 


admin.site.register(Evaluation)
admin.site.register(Enseignant)
admin.site.register(MaquetteGenerique)
admin.site.register(Matiere)
admin.site.register(Etudiant)
admin.site.register(Competence)
admin.site.register(Note)
admin.site.register(Ue)
admin.site.register(Semestre)
admin.site.register(Comptable)
admin.site.register(Tuteur)
admin.site.register(Personnel)
admin.site.register(AnneeUniversitaire)
