from django.db import models

class Evento(models.Model):

   nome = models.CharField(max_length=255)
   descricao = models.CharField(max_length=255)
   inicio = models.DateTimeField()
   final = models.DateTimeField()
