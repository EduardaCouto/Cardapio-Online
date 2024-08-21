from django.contrib.auth.models import User
from django.db import models
from restricao.models import Restricao


class Usuario(User):
    CATEGORIA_CHOICES = [
        ('CAE', 'CAE'),
        ('Nutricionista', 'Nutricionista'),
        ('Pessoa', 'Pessoa')    
    ]

    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='Pessoa')
    ### fruto da relação
    restricao = models.ForeignKey(Restricao, on_delete=models.SET_NULL, null=True, blank=True)



    def is_pessoa(self):
        return self.categoria == 'Pessoa'

    def is_cae(self):
        return self.categoria == 'CAE'

    def is_nutricionista(self):
        return self.categoria == 'Nutricionista'

    

