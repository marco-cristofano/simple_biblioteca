from django.db import models

GENERO = [
    ('DR', 'Drama'),
    ('RO', 'Romantico'),
    ('IN', 'Infantil'),
    ('CF', 'Ciencia Ficcion'),
    ('OT', 'Otro'),
]


class Autor(models.Model):
    nombre_fantasia = models.CharField(max_length=150)
    nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre_fantasia


class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    editorial = models.CharField(max_length=250)
    fecha_publicacion = models.DateField(null=True, blank=True)
    cantidad_paginas = models.PositiveIntegerField(null=True, blank=True)
    genero = models.CharField(
        max_length=2,
        choices=GENERO,
        default='OT'
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name='libros')

    def __str__(self):
        return self.titulo + ' ' + self.editorial
