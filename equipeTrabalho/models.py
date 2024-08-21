
from django.db import models

class Equipe(models.Model):
    FUNCAO_CHOICES = [
        ('Cozinha', 'Cozinha'),
        ('Servir almoço', 'Servir almoço'),
        ('Limpeza', 'Limpeza')    
    ]

    componentes = models.TextField()
    funcao = models.CharField(max_length=50, choices=FUNCAO_CHOICES, default='Cozinha')


