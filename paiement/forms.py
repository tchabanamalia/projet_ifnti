from typing import Any, Dict
import re
from typing import Any, Dict
from django import forms

from main.models import Comptable, Paiement, FicheDePaie
from .models import Evaluation, Note, Utilisateur, Personnel, Enseignant, Etudiant, Matiere, AnneeUniversitaire, Ue, Tuteur, Semestre
from django.core.exceptions import ValidationError
from django.forms import DateField
from django.forms.utils import ErrorList,ErrorDict
from django.forms.utils import ErrorList,ErrorDict
from django.utils.translation import gettext_lazy as _

class ComptableForm(forms.ModelForm):
    datenaissance = DateField(widget=forms.SelectDateWidget(years=range(1990, 2006)), label='Date de naissance')
    class Meta:
        model = Comptable
        fields = ['nom', 'prenom', 'contact', 'sexe', 'email', 'adresse', 'datenaissance', 'lieunaissance', 'prefecture', 'carte_identity', 'nationalite', 'salaireBrut', 'dernierdiplome', 'nbreJrsCongesRestant', 'nbreJrsConsomme', 'is_active']
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
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control col-md-6'}),
        }

    def clean(self):
        cleaned_data = super(ComptableForm, self).clean()
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
        is_active = cleaned_data.get('is_active')

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

        if nbreJrsCongesRestant > 30:
            if not 'nbreJrsCongesRestant' in self._errors:
                self._errors['nbreJrsCongesRestant'] = ErrorDict()
            self._errors['nbreJrsCongesRestant'] = 'Le nombre de jours de congés restant ne doit pas dépasser 30'

        if nbreJrsCongesRestant < 0:
            if not 'nbreJrsCongesRestant' in self._errors:
                self._errors['nbreJrsCongesRestant'] = ErrorDict()
            self._errors['nbreJrsCongesRestant'] = 'Le nombre de jours de congés restant ne doit pas être négatif'

        if nbreJrsConsomme < 0:
            if not 'nbreJrsConsommes' in self._errors:
                self._errors['nbreJrsConsommes'] = ErrorDict()
            self._errors['nbreJrsConsommes'] = 'Le nombre de jours de congés consommés ne doit pas être négatif'

        if nbreJrsConsomme > 30:
            if not 'nbreJrsConsommes' in self._errors:
                self._errors['nbreJrsConsommes'] = ErrorDict()
            self._errors['nbreJrsConsommes'] = 'Le nombre de jours de congés consommés ne doit pas dépasser 30'

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['type', 'montant','fraisconcours', 'fraisinscription', 'dateversement', 'nombreTranche', 'debit', 'credit', 'etudiant', 'comptable']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'fraisconcours': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'fraisinscription': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'dateversement': forms.DateInput(attrs={'class': 'form-control'}),
            'nombreTranche': forms.NumberInput(attrs={'class': 'form-control'}),
            'debit': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'credit': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),  # Ajout de 'readonly': True
            'etudiant': forms.Select(attrs={'class': 'form-control'}),
            'comptable': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PaiementForm, self).__init__(*args, **kwargs)
        self.fields['etudiant'].label_from_instance = lambda obj: f"{obj.nom} {obj.prenom}"
    
    def clean(self):
        cleaned_data = super(PaiementForm, self).clean()
        montant = cleaned_data.get('montant')
        fraisconcours = cleaned_data.get('fraisconcours')
        nombreTranche = cleaned_data.get('nombreTranche')
        debit = cleaned_data.get('debit')
        credit = cleaned_data.get('credit')
        etudiant = cleaned_data.get('etudiant')
        comptable = cleaned_data.get('comptable')

        if montant < 0:
            if not 'montant' in self._errors:
                self._errors['montant'] = ErrorDict()
            self._errors['montant'] = 'Le montant ne doit pas être négatif'

        if fraisconcours < 0:
            if not 'fraisconcours' in self._errors:
                self._errors['fraisconcours'] = ErrorDict()
            self._errors['fraisconcours'] = 'Les frais de concours ne doivent pas être négatifs'

        if nombreTranche < 0:
            if not 'nombreTranche' in self._errors:
                self._errors['nombreTranche'] = ErrorDict()
            self._errors['nombreTranche'] = 'Le nombre de tranche ne doit pas être négatif'

        if debit < 0:
            if not 'debit' in self._errors:
                self._errors['debit'] = ErrorDict()
            self._errors['debit'] = 'Le débit ne doit pas être négatif'

        if credit < 0:
            if not 'credit' in self._errors:
                self._errors['credit'] = ErrorDict()
            self._errors['credit'] = 'Le crédit ne doit pas être négatif'

        if montant > debit:
            if not 'montant' in self._errors:
                self._errors['montant'] = ErrorDict()
            self._errors['montant'] = 'Le montant ne doit pas être supérieur au débit'

        if debit == credit:
            if not 'debit' in self._errors:
                self._errors['debit'] = ErrorDict()
            self._errors['debit'] = 'Le débit ne doit pas être égal au crédit'

    
class FicheDePaieForm(forms.ModelForm):
    class Meta:
        model = FicheDePaie
        fields = ['dateDebut', 'dateFin','niveau1', 'niveau2', 'niveau3', 'bp', 'telephone',  'enseignant', 'prixUnitaire', 'montantAvance', 'montantAPayer', 'numero', 'heureL1', 'heureL2', 'heureL3', 'matiere', 'montantTotal', 'nombreHeure', 'montantL1', 'montantL2', 'montantL3', 'montantEnLettre']   
        widgets = {
            'dateDebut': forms.DateInput(attrs={'type': 'date'}),
            'dateFin': forms.DateInput(attrs={'type': 'date'}),
            'niveau1': forms.Select(choices=FicheDePaie.TYPE_CHOISE, attrs={'class': 'form-control'}),
            'niveau2': forms.Select(choices=FicheDePaie.TYPE_CHOISE1, attrs={'class': 'form-control'}),
            'niveau3': forms.Select(choices=FicheDePaie.TYPE_CHOISE2, attrs={'class': 'form-control'}),
            'bp': forms.NumberInput(attrs={'class': 'form-control'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control'}),
            'matiere': forms.TextInput(attrs={'class': 'form-control'}),
            'enseignant': forms.Select(attrs={'class': 'form-control'}),
            'nombreHeure': forms.NumberInput(attrs={'class': 'form-control'}),
            'prixUnitaire': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantTotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantAvance': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantAPayer': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantEnLettre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'heureL1': forms.NumberInput(attrs={'class': 'form-control'}),
            'heureL2': forms.NumberInput(attrs={'class': 'form-control'}),
            'heureL3': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantL1': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantL2': forms.NumberInput(attrs={'class': 'form-control'}),
            'montantL3': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        
