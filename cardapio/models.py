from django.db import models
from django.contrib.auth.models import User


class Cardapio(models.Model):
    data = models.DateField()  
    hora = models.TimeField() 
    proteina = models.CharField(max_length=100)  
    leguminosa = models.CharField(max_length=100) 
    carboidrato = models.CharField(max_length=100)  
    acompanhamento = models.CharField(max_length=100)  
    #fruto das relações
    nutricionista = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.proteina
