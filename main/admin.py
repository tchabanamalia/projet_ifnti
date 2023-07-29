from django.contrib import admin
from .models import Enseignant, Evaluation, Information, Programme, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, Paiement, FicheDePaie, DirecteurDesEtudes, Seance
from main.forms import EnseignantForm

admin.site.register(Evaluation)
class EnseignantAdmin(admin.ModelAdmin):
    form = EnseignantForm

admin.site.register(Programme)
admin.site.register(Enseignant, EnseignantAdmin)
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
admin.site.register(Information)
admin.site.register(Paiement)
admin.site.register(DirecteurDesEtudes)
admin.site.register(Seance)
admin.site.register(FicheDePaie)



