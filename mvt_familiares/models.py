from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    parentezco = models.CharField(max_length=25)
    fecha_nacimiento = models.CharField(max_length=10)
    dni = models.CharField(max_length=8)

