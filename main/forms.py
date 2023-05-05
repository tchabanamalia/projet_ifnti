from django import forms
from .models import Utilisateur, Personnel, Enseignant, Etudiant, Matiere, AnneeUniversitaire, Ue, Tuteur, Semestre
from django.core.exceptions import ValidationError
from django.forms import DateField
from django.utils.translation import gettext_lazy as _




class EtudiantForm(forms.ModelForm):
    datenaissance = DateField(widget=forms.SelectDateWidget(years=range(1900, 2006)), label="Date de naissance")

    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'contact', 'sexe', 'email', 'adresse', 'datenaissance', 'lieunaissance', 'prefecture', 'is_active', 'anneeentree', 'seriebac1', 'seriebac2', 'anneebac1', 'anneebac2', 'etablissementSeconde', 'etablissementPremiere', 'etablissementTerminale', 'francaisSeconde', 'francaisPremiere','francaisTerminale', 'anglaisSeconde', 'anglaisPremiere', 'anglaisTerminale', 'mathematiqueSeconde', 'mathematiquePremiere', 'mathematiqueTerminale']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'contact': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'sexe': forms.Select(choices=Etudiant.SEXE_CHOISE, attrs={'class': 'form-control col-md-6'}),
            'email': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'datenaissance': DateField(widget=forms.SelectDateWidget(years=range(1900, 2006)), label="Date de naissance"),
            'lieunaissance': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'prefecture': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'is_active': forms.CheckboxInput(),
            'anneeentree': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'seriebac1': forms.Select(choices=Etudiant.CHOIX_SERIE, attrs={'class': 'form-control col-md-6'}),
            'seriebac2': forms.Select(choices=Etudiant.CHOIX_SERIE, attrs={'class': 'form-control col-md-6'}), 
            'anneebac1': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'anneebac2': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'etablissementSeconde': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'etablissementPremiere': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'etablissementTerminale': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'francaisSeconde': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'francaisPremiere': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'francaisTerminale': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'anglaisSeconde': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'anglaisPremiere': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'anglaisTerminale': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'mathematiqueSeconde': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'mathematiquePremiere': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'mathematiqueTerminale': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
        }


   
    





class TuteurForm(forms.ModelForm):
    etudiants = forms.ModelMultipleChoiceField(queryset=Etudiant.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Tuteur
        fields = ['nom', 'prenom', 'contact', 'sexe', 'adresse', 'profession', 'type', 'etudiants']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'contact': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'sexe': forms.Select(choices=Tuteur.CHOIX_SEX, attrs={'class': 'form-control col-md-6'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'profession': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'type': forms.Select(choices=Tuteur.CHOIX_TYPE, attrs={'class': 'form-control col-md-6'}),
            'etudiants': forms.CheckboxSelectMultiple(),
        }




class UeForm(forms.ModelForm):
    enseignant = forms.ModelChoiceField(queryset=Enseignant.objects.all())
    semestre = forms.ModelChoiceField(queryset=Semestre.objects.all())
    class Meta:
        model = Ue
        fields = ['codeUE', 'libelle', 'nbreCredits', 'heures', 'enseignant', 'semestre']
        widgets = {
            'codeUE': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'libelle': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'nbreCredits': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'heures': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'enseignant': forms.Select(),
            'semestre': forms.Select(),
        }


class MatiereForm(forms.ModelForm):
    enseignant = forms.ModelChoiceField(queryset=Enseignant.objects.all())
    ue = forms.ModelChoiceField(queryset=Ue.objects.all())    
    class Meta:
        model = Matiere
        fields = ['codematiere', 'libelle', 'coefficient', 'minValue', 'enseignant', 'ue']
        widgets = {
            'codematiere': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'libelle': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'coefficient': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'minValue': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'enseignant': forms.Select(),
            'ue': forms.Select(),       
        }


class EnseignantForm(forms.ModelForm):
    datenaissance = DateField(widget=forms.SelectDateWidget(years=range(1990, 2006)), label='Date de naissance')

    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'contact', 'sexe', 'email', 'adresse', 'datenaissance', 'lieunaissance', 'prefecture', 'carte_identity', 'nationalite', 'salaireBrut', 'dernierdiplome', 'nbreJrsCongesRestant', 'nbreJrsConsomme', 'type', 'specialite', 'is_active']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'contact': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'sexe': forms.Select(attrs={'class': 'form-control col-md-6'}),
            'email': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'datenaissance': DateField(widget=forms.SelectDateWidget(years=range(1990, 2006)), label='Date de naissance'),
            'lieunaissance': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'prefecture': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'carte_identity': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'nationalite': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'salaireBrut': forms.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'dernierdiplome': forms.FileInput(attrs={'class': 'form-control col-md-6'}),
            'nbreJrsCongesRestant': forms.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'nbreJrsConsomme': forms.NumberInput(attrs={'class': 'form-control col-md-6'}),
            'type': forms.Select(attrs={'class': 'form-control col-md-6'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control col-md-6'}),
        }

