from django.db import models

class Alimento(models.Model):
    DISPONIBILIDADE_CHOICES = [
        ('Disponivel', 'Disponivel'),
        ('NaoDisponivel', 'NaoDisponivel')
 
    ]
    nome =  models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=50, choices=DISPONIBILIDADE_CHOICES)
    
