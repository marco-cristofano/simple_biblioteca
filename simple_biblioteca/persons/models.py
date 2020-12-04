from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
