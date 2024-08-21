from django import forms
from .models import Equipe

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        #  indica que todos os campos do modelo equipe serão usados no formulário.
        fields = '__all__'
