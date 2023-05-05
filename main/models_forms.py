
from django import forms 
from main.models import Etudiant, Matiere, Note


class NoteForm(forms.ModelForm):
    # etudiant = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'disabled': False, 'class' : 'form-input'})
    # )
    
    # matiere = forms.ModelChoiceField(
    #     queryset=Matiere.objects.all(),
    #     widget=forms.Select(attrs={'disabled': False, 'hidden' : False})
    # )
    
    class Meta:
        model = Note
        fields = ['valeurNote', 'matiere', 'etudiant']
        
    def clean(self):
        super().clean()

