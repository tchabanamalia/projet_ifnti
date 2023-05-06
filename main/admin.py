from django.contrib import admin

from main.forms import EnseignantForm
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique 

class EnseignantAdmin(admin.ModelAdmin):
    form = EnseignantForm
    
admin.site.register(Enseignant, EnseignantAdmin)
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


