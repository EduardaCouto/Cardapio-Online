from django import forms
from .models import Restricao


class EditRestricaoForm(forms.ModelForm):
    class Meta:
        model = Restricao
        fields = ['descricao','status']
