from django.db import models
from django.contrib.auth.models import User

class Restricao(models.Model):
    RESTRICAO_CHOICES = [
        ('Solicitado', 'Solicitado'),
        ('Andamento', 'Andamento'),
        ('Negado', 'Negado'),
        ('Aceito', 'Aceito')      
    ]

    descricao = models.TextField()
    status = models.CharField(max_length=50, choices=RESTRICAO_CHOICES, default='Solicitado')
