from rest_framework import serializers
from libros.models import (
    Autor,
    Libro
)


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = (
            'nombre_fantasia',
            'nacimiento'
        )


class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = (
            'titulo',
            'editorial',
            'fecha_publicacion',
            'cantidad_paginas',
            'genero',
            'autor'
        )


class LibroConAutorSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()

    class Meta:
        model = Libro
        fields = (
            'titulo',
            'editorial',
            'fecha_publicacion',
            'cantidad_paginas',
            'genero',
            'autor'
        )
