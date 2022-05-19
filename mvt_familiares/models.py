from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    parentezco = models.CharField(max_length=25)
    dni = models.IntegerField()

