from django import forms
from .models import Cardapio

class CardapioForm(forms.ModelForm):
    class Meta:
        model = Cardapio
        fields = ['data','hora', 'proteina', 'leguminosa', 'carboidrato','acompanhamento']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'HH:MM'}),
           
        }

