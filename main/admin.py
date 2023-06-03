from django.contrib import admin
from .models import Enseignant, Evaluation, Information, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique, Paiement
from main.forms import EnseignantForm
from .models import Enseignant, Matiere, Etudiant, Competence, Note, Comptable, Semestre, Ue, AnneeUniversitaire, Personnel, Tuteur, MaquetteGenerique, Paiement, Evaluation, Information

admin.site.register(Evaluation)
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
admin.site.register(Information)
admin.site.register(Paiement)



