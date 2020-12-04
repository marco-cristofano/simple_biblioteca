from rest_framework import serializers

from persons.models import Persona


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = (
            'nombre',
            'apellido',
            'dni'
        )


class MinimaPersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = (
            'nombre',
            'apellido'
        )
