from django import forms
from .models import Alimento

class AlimentosForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'
