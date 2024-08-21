from django.db import models
from django.contrib.auth.models import User
from cardapio.models import Cardapio

class Feedback(models.Model):
    comentario = models.TextField()
    #frutos das relações
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE) 