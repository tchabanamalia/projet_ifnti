
from django.forms import ModelForm
from main.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
    def clean(self):
        super().clean()