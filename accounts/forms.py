from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','nome', 'email','matricula','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nome = self.cleaned_data['nome']
        user.categoria = self.cleaned_data.get('categoria', 'Pessoa')  
        if commit:
            user.save()  

            grupo_usuario, created = Group.objects.get_or_create(name='usuario')

            user.groups.add(grupo_usuario)

        return user
