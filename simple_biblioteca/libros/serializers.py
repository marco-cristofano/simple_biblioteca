from rest_framework import serializers

from libros.models import (
    GENERO,
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


class LibroConAutorFullSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=250)
    editorial = serializers.CharField(max_length=250)
    fecha_publicacion = serializers.DateField(required=False)
    cantidad_paginas = serializers.IntegerField(min_value=0, required=False)
    genero = serializers.ChoiceField(choices=GENERO)
    nombre_fantasia = serializers.CharField(max_length=250)
    nacimiento = serializers.DateField(required=False)


class LibroConAutorlOutSerializer(LibroSerializer):
    nombre_fantasia = serializers.CharField(source='autor.nombre_fantasia')
    nacimiento = serializers.DateField(source='autor.nacimiento')

    class Meta:
        model = Libro
        fields = (
            'titulo',
            'editorial',
            'fecha_publicacion',
            'cantidad_paginas',
            'genero',
            'nombre_fantasia',
            'nacimiento'
        )
