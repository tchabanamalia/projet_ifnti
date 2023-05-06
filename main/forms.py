import re
from typing import Any, Dict
from django import forms
from .models import Utilisateur, Personnel, Enseignant, Etudiant, Matiere, AnneeUniversitaire, Ue, Tuteur, Semestre
from django.core.exceptions import ValidationError
from django.forms import DateField
from django.forms.utils import ErrorList,ErrorDict



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

    def clean(self):
        cleaned_data = super(EnseignantForm, self).clean()
        nom = cleaned_data.get('nom')
        prenom = cleaned_data.get('prenom')
        contact = cleaned_data.get('contact')
        email = cleaned_data.get('email')
        adresse = cleaned_data.get('adresse')
        lieunaissance = cleaned_data.get('lieunaissance')
        sexe = cleaned_data.get('sexe')
        prefecture = cleaned_data.get('prefecture')
        carte_identity = cleaned_data.get('carte_identity')
        nationalite = cleaned_data.get('nationalite')
        salaireBrut = cleaned_data.get('salaireBrut')
        nbreJrsCongesRestant = cleaned_data.get('nbreJrsCongesRestant')
        nbreJrsConsomme = cleaned_data.get('nbreJrsConsomme')
        type = cleaned_data.get('type')
        specialite = cleaned_data.get('specialite')

         
        if nom.find(';') != -1 or nom.find('/') != -1 or nom.find('.') != -1 or nom.find(',') != -1 or nom.find(':') != -1 or nom.find('!') != -1 or nom.find('?') != -1 or nom.find('*') != -1 or nom.find('+') != -1 or nom.find('=') != -1 or nom.find('@') != -1 or nom.find('#') != -1 or nom.find('$') != -1 or nom.find('%') != -1 or nom.find('&') != -1 or nom.find('(') != -1 or nom.find(')') != -1 or nom.find('_') != -1 or nom.find('<') != -1 or nom.find('>') != -1 or nom.find('|') != -1 or nom.find('~') != -1 or nom.find('^') != -1 or nom.find('{') != -1 or nom.find('}') != -1 or nom.find('[') != -1 or nom.find(']') != -1 or nom.find('"') != -1 or nom.find('\\') != -1 or nom.find('`') != -1:
            #forms.nom.errors = "Le nom ne doit pas contenir des caractères spéciaux"
            #print(self._errors)
            if not 'nom' in self._errors:
                self._errors['nom'] = ErrorDict()
            self._errors['nom'] = 'Le nom ne doit pas contenir des caractères spéciaux'


        if nom.find('0') != -1 or nom.find('1') != -1 or nom.find('2') != -1 or nom.find('3') != -1 or nom.find('4') != -1 or nom.find('5') != -1 or nom.find('6') != -1 or nom.find('7') != -1 or nom.find('8') != -1 or nom.find('9') != -1:
            if not 'nom' in self._errors:
                self._errors['nom'] = ErrorDict()
            self._errors['nom'] = 'Le nom ne doit pas contenir des chiffres'
        
        if prenom.find(';') != -1 or prenom.find('/') != -1 or prenom.find('.') != -1 or prenom.find(',') != -1 or prenom.find(':') != -1 or prenom.find('!') != -1 or prenom.find('?') != -1 or prenom.find('*') != -1 or prenom.find('+') != -1 or prenom.find('=') != -1 or prenom.find('@') != -1 or prenom.find('#') != -1 or prenom.find('$') != -1 or prenom.find('%') != -1 or prenom.find('&') != -1 or prenom.find('(') != -1 or prenom.find(')') != -1 or prenom.find('_') != -1 or prenom.find('<') != -1 or prenom.find('>') != -1 or prenom.find('|') != -1 or prenom.find('~') != -1 or prenom.find('^') != -1 or prenom.find('{') != -1 or prenom.find('}') != -1 or prenom.find('[') != -1 or prenom.find(']') != -1 or prenom.find('"') != -1 or prenom.find('\\') != -1 or prenom.find('`') != -1:
            if not 'prenom' in self._errors:
                self._errors['prenom'] = ErrorDict()
            self._errors['prenom'] = 'Le prénom ne doit pas contenir des caractères spéciaux'

        if prenom.find('0') != -1 or prenom.find('1') != -1 or prenom.find('2') != -1 or prenom.find('3') != -1 or prenom.find('4') != -1 or prenom.find('5') != -1 or prenom.find('6') != -1 or prenom.find('7') != -1 or prenom.find('8') != -1 or prenom.find('9') != -1:
            if not 'prenom' in self._errors:
                self._errors['prenom'] = ErrorDict()
            self._errors['prenom'] = 'Le prénom ne doit pas contenir des chiffres'

        if contact.find(';') != -1 or contact.find('/') != -1 or contact.find('.') != -1 or contact.find(',') != -1 or contact.find(':') != -1 or contact.find('!') != -1 or contact.find('?') != -1 or contact.find('*') != -1 or contact.find('`') != -1 or contact.find('=') != -1 or contact.find('@') != -1 or contact.find('#') != -1 or contact.find('$') != -1 or contact.find('%') != -1 or contact.find('&') != -1 or contact.find('(') != -1 or contact.find(')') != -1 or contact.find('_') != -1 or contact.find('<') != -1 or contact.find('>') != -1 or contact.find('|') != -1 or contact.find('~') != -1 or contact.find('^') != -1 or contact.find('{') != -1 or contact.find('}') != -1 or contact.find('[') != -1 or contact.find(']') != -1 or contact.find('"') != -1 or contact.find('\\') != -1 or contact.find(' ') != -1 or contact.find("'") != -1 :
            if not 'contact' in self._errors:
                self._errors['contact'] = ErrorDict()
            self._errors['contact'] = 'Le contact ne doit pas contenir des caractères spéciaux'

        if contact.find('a') != -1 or contact.find('b') != -1 or contact.find('c') != -1 or contact.find('d') != -1 or contact.find('e') != -1 or contact.find('f') != -1 or contact.find('g') != -1 or contact.find('h') != -1 or contact.find('i') != -1 or contact.find('j') != -1 or contact.find('k') != -1 or contact.find('l') != -1 or contact.find('m') != -1 or contact.find('n') != -1 or contact.find('o') != -1 or contact.find('p') != -1 or contact.find('q') != -1 or contact.find('r') != -1 or contact.find('s') != -1 or contact.find('t') != -1 or contact.find('u') != -1 or contact.find('v') != -1 or contact.find('w') != -1 or contact.find('x') != -1 or contact.find('y') != -1 or contact.find('z') != -1:
            if not 'contact' in self._errors:
                self._errors['contact'] = ErrorDict()
            self._errors['contact'] = 'Le contact ne doit pas contenir des lettres'

        if email.find(';') != -1 or email.find('/') != -1 or email.find(',') != -1 or email.find(':') != -1 or email.find('!') != -1 or email.find('?') != -1 or email.find('*') != -1 or email.find('+') != -1 or email.find('=') != -1 or email.find('#') != -1 or email.find('$') != -1 or email.find('%') != -1 or email.find('&') != -1 or email.find('(') != -1 or email.find(')') != -1 or email.find('_') != -1 or email.find('<') != -1 or email.find('>') != -1 or email.find('|') != -1 or email.find('~') != -1 or email.find('^') != -1 or email.find('{') != -1 or email.find('}') != -1 or email.find('[') != -1 or email.find(']') != -1 or email.find('"') != -1 or email.find('\\') != -1 or email.find(' ') != -1 or email.find("'") != -1 :
            if not 'email' in self._errors:
                self._errors['email'] = ErrorDict()
            self._errors['email'] = 'L\'email ne doit pas contenir des caractères spéciaux'

        if adresse.find(';') != -1 or adresse.find('/') != -1 or adresse.find(',') != -1 or adresse.find(':') != -1 or adresse.find('!') != -1 or adresse.find('?') != -1 or adresse.find('*') != -1 or adresse.find('+') != -1 or adresse.find('=') != -1 or adresse.find('#') != -1 or adresse.find('$') != -1 or adresse.find('%') != -1 or adresse.find('&') != -1 or adresse.find('(') != -1 or adresse.find(')') != -1 or adresse.find('_') != -1 or adresse.find('<') != -1 or adresse.find('>') != -1 or adresse.find('|') != -1 or adresse.find('~') != -1 or adresse.find('^') != -1 or adresse.find('{') != -1 or adresse.find('}') != -1 or adresse.find('[') != -1 or adresse.find(']') != -1 or adresse.find('"') != -1 or adresse.find('\\') != -1 or adresse.find("'") != -1 or adresse.find('@') != -1 :
            if not 'adresse' in self._errors:
                self._errors['adresse'] = ErrorDict()
            self._errors['adresse'] = 'L\'adresse ne doit pas contenir des caractères spéciaux'

        if lieunaissance.find(';') != -1 or lieunaissance.find('/') != -1 or lieunaissance.find(',') != -1 or lieunaissance.find(':') != -1 or lieunaissance.find('!') != -1 or lieunaissance.find('?') != -1 or lieunaissance.find('*') != -1 or lieunaissance.find('+') != -1 or lieunaissance.find('=') != -1 or lieunaissance.find('#') != -1 or lieunaissance.find('$') != -1 or lieunaissance.find('%') != -1 or lieunaissance.find('&') != -1 or lieunaissance.find('(') != -1 or lieunaissance.find(')') != -1 or lieunaissance.find('_') != -1 or lieunaissance.find('<') != -1 or lieunaissance.find('>') != -1 or lieunaissance.find('|') != -1 or lieunaissance.find('~') != -1 or lieunaissance.find('^') != -1 or lieunaissance.find('{') != -1 or lieunaissance.find('}') != -1 or lieunaissance.find('[') != -1 or lieunaissance.find(']') != -1 or lieunaissance.find('"') != -1 or lieunaissance.find('\\') != -1 or lieunaissance.find("'") != -1 or lieunaissance.find('@') != -1 :
            if not 'lieunaissance' in self._errors:
                self._errors['lieunaissance'] = ErrorDict()
            self._errors['lieunaissance'] = 'Le lieu de naissance ne doit pas contenir des caractères spéciaux'

        if sexe.find(';') != -1 or sexe.find('/') != -1 or sexe.find(',') != -1 or sexe.find(':') != -1 or sexe.find('!') != -1 or sexe.find('?') != -1 or sexe.find('*') != -1 or sexe.find('+') != -1 or sexe.find('=') != -1 or sexe.find('#') != -1 or sexe.find('$') != -1 or sexe.find('%') != -1 or sexe.find('&') != -1 or sexe.find('(') != -1 or sexe.find(')') != -1 or sexe.find('_') != -1 or sexe.find('<') != -1 or sexe.find('>') != -1 or sexe.find('|') != -1 or sexe.find('~') != -1 or sexe.find('^') != -1 or sexe.find('{') != -1 or sexe.find('}') != -1 or sexe.find('[') != -1 or sexe.find(']') != -1 or sexe.find('"') != -1 or sexe.find('\\') != -1 or sexe.find("'") != -1 or sexe.find('@') != -1 :
            if not 'sexe' in self._errors:
                self._errors['sexe'] = ErrorDict()
            self._errors['sexe'] = 'Le sexe ne doit pas contenir des caractères spéciaux'

        if sexe.find('0') != -1 or sexe.find('1') != -1 or sexe.find('2') != -1 or sexe.find('3') != -1 or sexe.find('4') != -1 or sexe.find('5') != -1 or sexe.find('6') != -1 or sexe.find('7') != -1 or sexe.find('8') != -1 or sexe.find('9') != -1 :
            if not 'sexe' in self._errors:
                self._errors['sexe'] = ErrorDict()
            self._errors['sexe'] = 'Le sexe ne doit pas contenir des chiffres'

        if prefecture.find(';') != -1 or prefecture.find('/') != -1 or prefecture.find(',') != -1 or prefecture.find(':') != -1 or prefecture.find('!') != -1 or prefecture.find('?') != -1 or prefecture.find('*') != -1 or prefecture.find('+') != -1 or prefecture.find('=') != -1 or prefecture.find('#') != -1 or prefecture.find('$') != -1 or prefecture.find('%') != -1 or prefecture.find('&') != -1 or prefecture.find('(') != -1 or prefecture.find(')') != -1 or prefecture.find('_') != -1 or prefecture.find('<') != -1 or prefecture.find('>') != -1 or prefecture.find('|') != -1 or prefecture.find('~') != -1 or prefecture.find('^') != -1 or prefecture.find('{') != -1 or prefecture.find('}') != -1 or prefecture.find('[') != -1 or prefecture.find(']') != -1 or prefecture.find('"') != -1 or prefecture.find('\\') != -1 or prefecture.find("'") != -1 or prefecture.find('@') != -1 :
            if not 'prefecture' in self._errors:
                self._errors['prefecture'] = ErrorDict()
            self._errors['prefecture'] = 'La préfecture ne doit pas contenir des caractères spéciaux'

        if nationalite.find(';') != -1 or nationalite.find('/') != -1 or nationalite.find(',') != -1 or nationalite.find(':') != -1 or nationalite.find('!') != -1 or nationalite.find('?') != -1 or nationalite.find('*') != -1 or nationalite.find('+') != -1 or nationalite.find('=') != -1 or nationalite.find('#') != -1 or nationalite.find('$') != -1 or nationalite.find('%') != -1 or nationalite.find('&') != -1 or nationalite.find('(') != -1 or nationalite.find(')') != -1 or nationalite.find('_') != -1 or nationalite.find('<') != -1 or nationalite.find('>') != -1 or nationalite.find('|') != -1 or nationalite.find('~') != -1 or nationalite.find('^') != -1 or nationalite.find('{') != -1 or nationalite.find('}') != -1 or nationalite.find('[') != -1 or nationalite.find(']') != -1 or nationalite.find('"') != -1 or nationalite.find('\\') != -1 or nationalite.find("'") != -1 or nationalite.find('@') != -1 :
            if not 'nationalite' in self._errors:
                self._errors['nationalite'] = ErrorDict()
            self._errors['nationalite'] = 'La nationalité ne doit pas contenir des caractères spéciaux'

        if nationalite.find('0') != -1 or nationalite.find('1') != -1 or nationalite.find('2') != -1 or nationalite.find('3') != -1 or nationalite.find('4') != -1 or nationalite.find('5') != -1 or nationalite.find('6') != -1 or nationalite.find('7') != -1 or nationalite.find('8') != -1 or nationalite.find('9') != -1 :
            if not 'nationalite' in self._errors:
                self._errors['nationalite'] = ErrorDict()
            self._errors['nationalite'] = 'La nationalité ne doit pas contenir des chiffres'

        if carte_identity.find(';') != -1 or carte_identity.find('/') != -1 or carte_identity.find(',') != -1 or carte_identity.find(':') != -1 or carte_identity.find('!') != -1 or carte_identity.find('?') != -1 or carte_identity.find('*') != -1 or carte_identity.find('+') != -1 or carte_identity.find('=') != -1 or carte_identity.find('#') != -1 or carte_identity.find('$') != -1 or carte_identity.find('%') != -1 or carte_identity.find('&') != -1 or carte_identity.find('(') != -1 or carte_identity.find(')') != -1 or carte_identity.find('_') != -1 or carte_identity.find('<') != -1 or carte_identity.find('>') != -1 or carte_identity.find('|') != -1 or carte_identity.find('~') != -1 or carte_identity.find('^') != -1 or carte_identity.find('{') != -1 or carte_identity.find('}') != -1 or carte_identity.find('[') != -1 or carte_identity.find(']') != -1 or carte_identity.find('"') != -1 or carte_identity.find('\\') != -1 or carte_identity.find("'") != -1 or carte_identity.find('@') != -1 :
            if not 'carte_identity' in self._errors:
                self._errors['carte_identity'] = ErrorDict()
            self._errors['carte_identity'] = 'La carte d\'identité ne doit pas contenir des caractères spéciaux'

        if carte_identity.find('A') != -1 or carte_identity.find('B') != -1 or carte_identity.find('C') != -1 or carte_identity.find('D') != -1 or carte_identity.find('E') != -1 or carte_identity.find('F') != -1 or carte_identity.find('G') != -1 or carte_identity.find('H') != -1 or carte_identity.find('I') != -1 or carte_identity.find('J') != -1 or carte_identity.find('K') != -1 or carte_identity.find('L') != -1 or carte_identity.find('M') != -1 or carte_identity.find('N') != -1 or carte_identity.find('O') != -1 or carte_identity.find('P') != -1 or carte_identity.find('Q') != -1 or carte_identity.find('R') != -1 or carte_identity.find('S') != -1 or carte_identity.find('T') != -1 or carte_identity.find('U') != -1 or carte_identity.find('V') != -1 or carte_identity.find('W') != -1 or carte_identity.find('X') != -1 or carte_identity.find('Y') != -1 or carte_identity.find('Z') != -1 :
            if not 'carte_identity' in self._errors:
                self._errors['carte_identity'] = ErrorDict()
            self._errors['carte_identity'] = 'La carte d\'identité ne doit pas contenir des lettres majuscules'

        if carte_identity.find('a') != -1 or carte_identity.find('b') != -1 or carte_identity.find('c') != -1 or carte_identity.find('d') != -1 or carte_identity.find('e') != -1 or carte_identity.find('f') != -1 or carte_identity.find('g') != -1 or carte_identity.find('h') != -1 or carte_identity.find('i') != -1 or carte_identity.find('j') != -1 or carte_identity.find('k') != -1 or carte_identity.find('l') != -1 or carte_identity.find('m') != -1 or carte_identity.find('n') != -1 or carte_identity.find('o') != -1 or carte_identity.find('p') != -1 or carte_identity.find('q') != -1 or carte_identity.find('r') != -1 or carte_identity.find('s') != -1 or carte_identity.find('t') != -1 or carte_identity.find('u') != -1 or carte_identity.find('v') != -1 or carte_identity.find('w') != -1 or carte_identity.find('x') != -1 or carte_identity.find('y') != -1 or carte_identity.find('z') != -1 :
            if not 'carte_identity' in self._errors:
                self._errors['carte_identity'] = ErrorDict()
            self._errors['carte_identity'] = 'La carte d\'identité ne doit pas contenir des lettres minuscules'

        if salaireBrut < 0:
            if not 'salaireBrut' in self._errors:
                self._errors['salaireBrut'] = ErrorDict()
            self._errors['salaireBrut'] = 'Le salaire ne doit pas être inférieur à 0'

        if nbreJrsCongesRestant > 30:
            if not 'nbreJrsCongesRestant' in self._errors:
                self._errors['nbreJrsCongesRestant'] = ErrorDict()
            self._errors['nbreJrsCongesRestant'] = 'Le nombre de jours de congés restant ne doit pas être supérieur à 30'

        if nbreJrsCongesRestant < 0:
            if not 'nbreJrsCongesRestant' in self._errors:
                self._errors['nbreJrsCongesRestant'] = ErrorDict()
            self._errors['nbreJrsCongesRestant'] = 'Le nombre de jours de congés restant ne doit pas être inférieur à 0'

        if nbreJrsConsomme > 30:
            if not 'nbreJrsConsomme' in self._errors:
                self._errors['nbreJrsConsomme'] = ErrorDict()
            self._errors['nbreJrsConsomme'] = 'Le nombre de jours de congés consommés ne doit pas être supérieur à 30'

        if nbreJrsConsomme < 0:
            if not 'nbreJrsConsomme' in self._errors:
                self._errors['nbreJrsConsomme'] = ErrorDict()
            self._errors['nbreJrsConsomme'] = 'Le nombre de jours de congés consommés ne doit pas être inférieur à 0'
        
        if type.find(';') != -1 or type.find(':') != -1 or type.find('!') != -1 or type.find('?') != -1 or type.find('.') != -1 or type.find(',') != -1 or type.find('/') != -1 or type.find('§') != -1 or type.find('*') != -1 or type.find('+') != -1 or type.find('-') != -1 or type.find('=') != -1 or type.find('\'') != -1 or type.find('\"') != -1 or type.find('[') != -1 or type.find(']') != -1 or type.find('{') != -1 or type.find('}') != -1 or type.find('(') != -1 or type.find(')') != -1 or type.find('°') != -1 or type.find('€') != -1 or type.find('$') != -1 or type.find('£') != -1 or type.find('¤') != -1 or type.find('`') != -1 or type.find('²') != -1 or type.find('³') != -1 or type.find('£') != -1 or type.find('%') != -1 or type.find('µ') != -1 or type.find('§') != -1 or type.find('!') != -1 or type.find(':') != -1 or type.find('/') != -1 or type.find('§') != -1 or type.find(' ') != -1:
            if not 'type' in self._errors:
                self._errors['type'] = ErrorDict()
            self._errors['type'] = 'Le type ne doit pas contenir des caractères spéciaux'

        if type.find('0') != -1 or type.find('1') != -1 or type.find('2') != -1 or type.find('3') != -1 or type.find('4') != -1 or type.find('5') != -1 or type.find('6') != -1 or type.find('7') != -1 or type.find('8') != -1 or type.find('9') != -1:
            if not 'type' in self._errors:
                self._errors['type'] = ErrorDict()
            self._errors['type'] = 'Le type ne doit pas contenir des chiffres'

        if specialite.find(';') != -1 or specialite.find(':') != -1 or specialite.find('!') != -1 or specialite.find('?') != -1 or specialite.find('.') != -1 or specialite.find(',') != -1 or specialite.find('/') != -1 or specialite.find('§') != -1 or specialite.find('*') != -1 or specialite.find('+') != -1 or specialite.find('-') != -1 or specialite.find('=') != -1 or specialite.find('\'') != -1 or specialite.find('\"') != -1 or specialite.find('[') != -1 or specialite.find(']') != -1 or specialite.find('{') != -1 or specialite.find('}') != -1 or specialite.find('(') != -1 or specialite.find(')') != -1 or specialite.find('°') != -1 or specialite.find('€') != -1 or specialite.find('$') != -1 or specialite.find('£') != -1 or specialite.find('¤') != -1 or specialite.find('`') != -1 or specialite.find('²') != -1 or specialite.find('³') != -1 or specialite.find('£') != -1 or specialite.find('%') != -1 or specialite.find('µ') != -1 or specialite.find('§') != -1 or specialite.find('!') != -1 or specialite.find(':') != -1 or specialite.find('/') != -1 or specialite.find('§') != -1 or specialite.find(' ') != -1:
            if not 'specialite' in self._errors:
                self._errors['specialite'] = ErrorDict()
            self._errors['specialite'] = 'La spécialité ne doit pas contenir des caractères spéciaux'

        if specialite.find('0') != -1 or specialite.find('1') != -1 or specialite.find('2') != -1 or specialite.find('3') != -1 or specialite.find('4') != -1 or specialite.find('5') != -1 or specialite.find('6') != -1 or specialite.find('7') != -1 or specialite.find('8') != -1 or specialite.find('9') != -1:
            if not 'specialite' in self._errors:
                self._errors['specialite'] = ErrorDict()
            self._errors['specialite'] = 'La spécialité ne doit pas contenir des chiffres'

        

        

        

