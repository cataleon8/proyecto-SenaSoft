
from django import forms
from .models import Competidor

class CompetidorForm(forms.ModelForm):

    class Meta:
        model = Competidor
        fields = ['nombre', 'centro', 'categoria']



