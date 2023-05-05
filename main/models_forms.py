
from django import forms 
from main.models import Etudiant, Matiere, Note


class NoteForm(forms.ModelForm):
    etudiant = forms.ModelChoiceField(
        queryset=Etudiant.objects.all(),
        widget=forms.Select(attrs={'disabled': False, 'class' : 'form-select'})
    )
    
    matiere = forms.ModelChoiceField(
        queryset=Matiere.objects.all(),
        widget=forms.Select(attrs={'disabled': False, 'hidden' : False})
    )
    
    class Meta:
        model = Note
        fields = ['etudiant', 'valeurNote', 'matiere', 'id']
        
    def clean(self):
        super().clean()

